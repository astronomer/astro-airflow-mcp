"""Airflow version detection for multi-version support."""

import logging
from typing import Literal

import httpx
from packaging.version import Version

logger = logging.getLogger(__name__)

AirflowMajorVersion = Literal[2, 3]


def detect_airflow_version(
    airflow_url: str,
    auth_token: str | None = None,
    username: str | None = None,
    password: str | None = None,
) -> tuple[AirflowMajorVersion, str]:
    """Detect Airflow version from the API.

    Args:
        airflow_url: Base URL of Airflow webserver (e.g., http://localhost:8080)
        auth_token: Optional Bearer token for authentication
        username: Optional username for basic auth
        password: Optional password for basic auth

    Returns:
        Tuple of (major_version, full_version_string)

    Raises:
        RuntimeError: If version cannot be detected or is unsupported

    Note:
        Airflow 2.x uses /api/v1/version
        Airflow 3.x uses /api/v2/version
        This function tries v2 first, then falls back to v1.
    """
    headers = {}
    auth = None

    # Set up authentication
    if username and password:
        # Use basic auth (typical for Airflow 2.x)
        auth = (username, password)
    elif auth_token:
        # Use Bearer token auth
        headers["Authorization"] = f"Bearer {auth_token}"

    # Try both API versions (v2 for Airflow 3.x, v1 for Airflow 2.x)
    last_error: Exception | None = None
    empty_version_found = False

    for api_version in ["v2", "v1"]:
        version_url = f"{airflow_url}/api/{api_version}/version"

        try:
            response = httpx.get(version_url, headers=headers, auth=auth, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            version_string = data.get("version", "")

            if not version_string:
                empty_version_found = True
                continue  # Try next API version

            version = Version(version_string)
            major = version.major

            if major not in (2, 3):
                raise RuntimeError(
                    f"Unsupported Airflow version: {version_string} (only 2.9+ and 3.x supported)"
                )

            logger.info(
                f"Detected Airflow {major}.x (full version: {version_string}) via /api/{api_version}/version"
            )
            # Cast to AirflowMajorVersion since we've verified it's 2 or 3
            return major, version_string  # type: ignore[return-value]

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                # This API version doesn't exist, try the next one
                last_error = e
                continue
            # Other HTTP errors should be raised
            raise RuntimeError(f"Failed to detect Airflow version from {version_url}: {e}") from e
        except httpx.HTTPError as e:
            last_error = e
            continue
        except Exception as e:
            raise RuntimeError(f"Error parsing Airflow version from {version_url}: {e}") from e

    # If we get here, both API versions failed
    if empty_version_found:
        raise RuntimeError("Version string empty in API response")

    raise RuntimeError(
        f"Failed to detect Airflow version. Tried /api/v2/version and /api/v1/version. "
        f"Last error: {last_error}"
    )


class VersionCache:
    """Cache for detected Airflow version to avoid repeated API calls."""

    def __init__(self):
        self._major_version: AirflowMajorVersion | None = None
        self._full_version: str | None = None

    def get(self) -> tuple[AirflowMajorVersion, str] | None:
        """Get cached version info."""
        if self._major_version is None:
            return None
        return self._major_version, self._full_version

    def set(self, major: AirflowMajorVersion, full: str) -> None:
        """Cache version info."""
        self._major_version = major
        self._full_version = full

    def clear(self) -> None:
        """Clear cached version (useful for testing)."""
        self._major_version = None
        self._full_version = None


# Global version cache
_version_cache = VersionCache()


def get_or_detect_version(
    airflow_url: str,
    auth_token: str | None = None,
    username: str | None = None,
    password: str | None = None,
) -> tuple[AirflowMajorVersion, str]:
    """Get cached version or detect if not yet cached.

    Args:
        airflow_url: Base URL of Airflow webserver
        auth_token: Optional Bearer token
        username: Optional username for basic auth
        password: Optional password for basic auth

    Returns:
        Tuple of (major_version, full_version_string)
    """
    cached = _version_cache.get()
    if cached is not None:
        return cached

    major, full = detect_airflow_version(airflow_url, auth_token, username, password)
    _version_cache.set(major, full)
    return major, full

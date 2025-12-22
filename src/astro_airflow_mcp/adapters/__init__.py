"""Adapter factory for creating version-specific Airflow clients."""

import httpx

from astro_airflow_mcp.adapters.airflow_v2 import AirflowV2Adapter
from astro_airflow_mcp.adapters.airflow_v3 import AirflowV3Adapter
from astro_airflow_mcp.adapters.base import AirflowAdapter, NotFoundError


def _get_jwt_token(airflow_url: str, username: str, password: str) -> str | None:
    """Attempt to get a JWT token via OAuth2 (Airflow 3 style).

    Args:
        airflow_url: Base URL of Airflow webserver
        username: Airflow username
        password: Airflow password

    Returns:
        JWT access token if successful, None otherwise
    """
    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.post(
                f"{airflow_url}/auth/token",
                data={"username": username, "password": password},
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            if response.status_code == 200:
                data = response.json()
                return data.get("access_token")
    except Exception:  # noqa: S110 - intentionally silent, fallback to other auth
        return None
    return None


def detect_version(
    airflow_url: str,
    auth_token: str | None = None,
    username: str | None = None,
    password: str | None = None,
) -> tuple[int, str]:
    """Detect Airflow version by probing API endpoints.

    Auth strategy:
    - If auth_token is provided, use it as Bearer token
    - For Airflow 3: Try OAuth2 token exchange (username/password -> JWT)
    - For Airflow 2: Use basic auth (username/password)

    Args:
        airflow_url: Base URL of Airflow webserver
        auth_token: Optional Bearer token
        username: Optional username for auth
        password: Optional password for auth

    Returns:
        Tuple of (major_version, full_version_string)

    Raises:
        RuntimeError: If version detection fails
    """
    headers: dict[str, str] = {}
    auth: tuple[str, str] | None = None

    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"

    # Try Airflow 3 API first (/api/v2/version)
    # Airflow 3 uses OAuth2 - try to get JWT if we have username/password
    jwt_token = None
    if not auth_token and username and password:
        jwt_token = _get_jwt_token(airflow_url, username, password)
        if jwt_token:
            headers["Authorization"] = f"Bearer {jwt_token}"

    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.get(
                f"{airflow_url}/api/v2/version",
                headers=headers,
            )
            if response.status_code == 200:
                data = response.json()
                version = data.get("version", "3.0.0")
                major = int(version.split(".")[0])
                return (major, version)
    except Exception:  # nosec B110 - try v2 API next
        pass

    # Try Airflow 2 API (/api/v1/version)
    # Airflow 2 uses basic auth
    headers_v2: dict[str, str] = {}
    if auth_token:
        headers_v2["Authorization"] = f"Bearer {auth_token}"
    elif username and password:
        auth = (username, password)
    else:
        # Default to admin:admin for Airflow 2 (common dev default)
        auth = ("admin", "admin")  # noqa: S105

    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.get(
                f"{airflow_url}/api/v1/version",
                headers=headers_v2,
                auth=auth,
            )
            if response.status_code == 200:
                data = response.json()
                version = data.get("version", "2.0.0")
                major = int(version.split(".")[0])
                return (major, version)
    except Exception:  # nosec B110 - raise RuntimeError below
        pass

    raise RuntimeError(
        f"Failed to detect Airflow version at {airflow_url}. "
        "Ensure Airflow is running and accessible."
    )


def create_adapter(
    airflow_url: str,
    auth_token: str | None = None,
    username: str | None = None,
    password: str | None = None,
) -> AirflowAdapter:
    """Create appropriate adapter based on detected Airflow version.

    Args:
        airflow_url: Base URL of Airflow webserver
        auth_token: Optional Bearer token (alternative to username/password)
        username: Optional username for basic auth
        password: Optional password for basic auth

    Returns:
        Version-specific adapter instance

    Raises:
        RuntimeError: If version detection fails or version is unsupported

    Note:
        - Airflow 2.x typically requires basic auth (defaults to admin:admin if not provided)
        - Airflow 3.x is typically open (no auth) unless explicitly configured
    """
    major_version, full_version = detect_version(
        airflow_url, auth_token=auth_token, username=username, password=password
    )

    # Apply version-specific auth defaults
    if major_version == 2:
        # Airflow 2.x typically requires basic auth
        if not auth_token and not username and not password:
            # Default Airflow 2 dev credentials
            username = "admin"  # nosec B105
            password = "admin"  # nosec B105
        return AirflowV2Adapter(
            airflow_url,
            full_version,
            auth_token=auth_token,
            username=username,
            password=password,
        )
    elif major_version >= 3:
        return AirflowV3Adapter(
            airflow_url,
            full_version,
            auth_token=auth_token,
            username=username,
            password=password,
        )
    else:
        raise RuntimeError(f"Unsupported Airflow version: {major_version}")


__all__ = [
    "AirflowAdapter",
    "AirflowV2Adapter",
    "AirflowV3Adapter",
    "NotFoundError",
    "create_adapter",
    "detect_version",
]

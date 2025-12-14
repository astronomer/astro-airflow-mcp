"""Adapter factory for creating version-specific Airflow clients."""

from astro_airflow_mcp.adapters.airflow_v2_adapter import AirflowV2Adapter
from astro_airflow_mcp.adapters.airflow_v3_adapter import AirflowV3Adapter
from astro_airflow_mcp.adapters.base import AirflowAdapter
from astro_airflow_mcp.version_detection import get_or_detect_version


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
    major_version, full_version = get_or_detect_version(
        airflow_url, auth_token=auth_token, username=username, password=password
    )

    # Apply version-specific auth defaults
    if major_version == 2:
        # Airflow 2.x typically requires basic auth - default to admin:admin if not provided
        if not auth_token and not username and not password:
            username = "admin"  # nosec B105
            password = "admin"  # nosec B105
        return AirflowV2Adapter(
            airflow_url, auth_token=auth_token, username=username, password=password
        )
    elif major_version == 3:
        # Airflow 3.x is typically open (no auth) - only pass credentials if explicitly provided
        return AirflowV3Adapter(
            airflow_url, auth_token=auth_token, username=username, password=password
        )
    else:
        raise RuntimeError(f"Unsupported Airflow version: {major_version}")


__all__ = ["AirflowAdapter", "AirflowV2Adapter", "AirflowV3Adapter", "create_adapter"]

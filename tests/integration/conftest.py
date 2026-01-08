"""Pytest fixtures for integration tests."""

import os

import pytest

# Skip integration tests if AIRFLOW_URL is not set
pytestmark = pytest.mark.skipif(
    os.getenv("AIRFLOW_URL") is None,
    reason="Integration tests require AIRFLOW_URL environment variable",
)


@pytest.fixture
def airflow_url() -> str:
    """Get Airflow URL from environment."""
    return os.getenv("AIRFLOW_URL", "http://localhost:8080")


@pytest.fixture
def airflow_username() -> str:
    """Get Airflow username from environment."""
    return os.getenv("AIRFLOW_USERNAME", "admin")


@pytest.fixture
def airflow_password() -> str:
    """Get Airflow password from environment."""
    return os.getenv("AIRFLOW_PASSWORD", "admin")


@pytest.fixture
def airflow_version() -> str:
    """Get expected Airflow version from environment."""
    return os.getenv("AIRFLOW_VERSION", "")


@pytest.fixture
def airflow_api_path() -> str:
    """Get API path based on version."""
    return os.getenv("AIRFLOW_API_PATH", "/api/v1")


@pytest.fixture
def airflow_auth_method() -> str:
    """Get auth method (basic or oauth2)."""
    return os.getenv("AIRFLOW_AUTH_METHOD", "basic")

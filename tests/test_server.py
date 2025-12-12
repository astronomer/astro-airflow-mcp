"""Tests for server API client wrapper."""

import json

from astro_airflow_mcp.server import (
    AirflowConfig,
    _get_dag_details_impl,
    _list_dags_impl,
    configure,
)


class TestImplFunctions:
    """Tests for _impl functions using mocked adapter."""

    def test_get_dag_details_impl_success(self, mocker):
        """Test _get_dag_details_impl with successful response."""
        from astro_airflow_mcp.server import _config

        mock_dag_data = {
            "dag_id": "example_dag",
            "is_paused": False,
            "description": "Test DAG",
        }
        # Mock the adapter's get_dag method
        mock_adapter = mocker.Mock()
        mock_adapter.get_dag.return_value = mock_dag_data

        # Patch the private _adapter attribute
        original_adapter = _config._adapter
        _config._adapter = mock_adapter
        try:
            result = _get_dag_details_impl("example_dag")
            result_data = json.loads(result)

            assert result_data["dag_id"] == "example_dag"
            assert result_data["is_paused"] is False
            assert result_data["description"] == "Test DAG"
        finally:
            _config._adapter = original_adapter

    def test_get_dag_details_impl_error(self, mocker):
        """Test _get_dag_details_impl with API error."""
        from astro_airflow_mcp.server import _config

        # Mock the adapter's get_dag method to raise an exception
        mock_adapter = mocker.Mock()
        mock_adapter.get_dag.side_effect = Exception("DAG not found")

        # Patch the private _adapter attribute
        original_adapter = _config._adapter
        _config._adapter = mock_adapter
        try:
            result = _get_dag_details_impl("nonexistent_dag")
            assert "DAG not found" in result
        finally:
            _config._adapter = original_adapter

    def test_list_dags_impl_success(self, mocker):
        """Test _list_dags_impl with successful response."""
        from astro_airflow_mcp.server import _config

        mock_response = {
            "dags": [
                {"dag_id": "dag1", "is_paused": False},
                {"dag_id": "dag2", "is_paused": True},
            ],
            "total_entries": 2,
        }
        # Mock the adapter's list_dags method
        mock_adapter = mocker.Mock()
        mock_adapter.list_dags.return_value = mock_response

        # Patch the private _adapter attribute
        original_adapter = _config._adapter
        _config._adapter = mock_adapter
        try:
            result = _list_dags_impl(limit=10, offset=0)
            result_data = json.loads(result)

            assert result_data["total_dags"] == 2
            assert result_data["returned_count"] == 2
            assert len(result_data["dags"]) == 2
            assert result_data["dags"][0]["dag_id"] == "dag1"
        finally:
            _config._adapter = original_adapter

    def test_list_dags_impl_empty(self, mocker):
        """Test _list_dags_impl with no DAGs."""
        from astro_airflow_mcp.server import _config

        mock_response = {"dags": [], "total_entries": 0}
        # Mock the adapter's list_dags method
        mock_adapter = mocker.Mock()
        mock_adapter.list_dags.return_value = mock_response

        # Patch the private _adapter attribute
        original_adapter = _config._adapter
        _config._adapter = mock_adapter
        try:
            result = _list_dags_impl()
            result_data = json.loads(result)

            assert result_data["total_dags"] == 0
            assert result_data["returned_count"] == 0
            assert result_data["dags"] == []
        finally:
            _config._adapter = original_adapter


class TestConfiguration:
    """Tests for global configuration."""

    def test_configure_url(self):
        """Test configure() updates global URL."""
        from astro_airflow_mcp.server import _config

        original_url = _config.url
        original_adapter = _config._adapter
        try:
            configure(url="https://test.airflow.com")
            assert _config.url == "https://test.airflow.com"
            # Verify adapter was reset
            assert _config._adapter is None
        finally:
            # Restore original
            _config.url = original_url
            _config._adapter = original_adapter

    def test_configure_auth_token(self):
        """Test configure() updates global auth token."""
        from astro_airflow_mcp.server import _config

        original_token = _config.auth_token
        original_adapter = _config._adapter
        try:
            configure(auth_token="new_token_456")
            assert _config.auth_token == "new_token_456"
            # Verify adapter was reset
            assert _config._adapter is None
        finally:
            # Restore original
            _config.auth_token = original_token
            _config._adapter = original_adapter

    def test_configure_username_password(self):
        """Test configure() updates username and password."""
        from astro_airflow_mcp.server import _config

        original_username = _config.username
        original_password = _config.password
        original_adapter = _config._adapter
        try:
            configure(username="testuser", password="testpass")
            assert _config.username == "testuser"
            assert _config.password == "testpass"
            # Verify adapter was reset
            assert _config._adapter is None
        finally:
            # Restore originals
            _config.username = original_username
            _config.password = original_password
            _config._adapter = original_adapter

    def test_configure_all_params(self):
        """Test configure() updates all parameters."""
        from astro_airflow_mcp.server import _config

        original_url = _config.url
        original_token = _config.auth_token
        original_username = _config.username
        original_password = _config.password
        original_adapter = _config._adapter
        try:
            configure(
                url="https://prod.airflow.com",
                auth_token="prod_token",
                username="produser",
                password="prodpass",
            )
            assert _config.url == "https://prod.airflow.com"
            assert _config.auth_token == "prod_token"
            assert _config.username == "produser"
            assert _config.password == "prodpass"
            # Verify adapter was reset
            assert _config._adapter is None
        finally:
            # Restore originals
            _config.url = original_url
            _config.auth_token = original_token
            _config.username = original_username
            _config.password = original_password
            _config._adapter = original_adapter

    def test_default_username_password(self):
        """Test default username and password are None (version-specific defaults applied later)."""

        config = AirflowConfig()
        assert config.username is None
        assert config.password is None

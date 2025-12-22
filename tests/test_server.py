"""Tests for server API client wrapper."""

import json

import httpx
import pytest

from astro_airflow_mcp.server import (
    DEFAULT_AIRFLOW_URL,
    _call_airflow_api,
    _get_dag_details_impl,
    _list_dags_impl,
    configure,
)


class TestCallAirflowAPI:
    """Tests for the _call_airflow_api function."""

    def test_basic_api_call(self, mocker):
        """Test basic API call without authentication."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"dags": []}
        mock_response.raise_for_status = mocker.Mock()
        mock_response.status_code = 200

        mock_client = mocker.Mock()
        mock_client.get.return_value = mock_response
        mock_client.__enter__ = mocker.Mock(return_value=mock_client)
        mock_client.__exit__ = mocker.Mock(return_value=False)

        mocker.patch("httpx.Client", return_value=mock_client)

        result = _call_airflow_api("dags")

        assert result == {"dags": []}
        mock_client.get.assert_called_once_with(
            f"{DEFAULT_AIRFLOW_URL}/api/v2/dags",
            params=None,
            headers={},
            auth=None,
        )

    def test_api_call_with_auth_token(self, mocker):
        """Test API call with Bearer token authentication."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"version": "3.0.0"}
        mock_response.raise_for_status = mocker.Mock()
        mock_response.status_code = 200

        mock_client = mocker.Mock()
        mock_client.get.return_value = mock_response
        mock_client.__enter__ = mocker.Mock(return_value=mock_client)
        mock_client.__exit__ = mocker.Mock(return_value=False)

        mocker.patch("httpx.Client", return_value=mock_client)

        result = _call_airflow_api("version", auth_token="test_token_123")

        assert result == {"version": "3.0.0"}
        mock_client.get.assert_called_once()
        call_kwargs = mock_client.get.call_args[1]
        assert call_kwargs["headers"]["Authorization"] == "Bearer test_token_123"

    def test_api_call_with_basic_auth(self, mocker):
        """Test API call with basic auth (username/password)."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"version": "2.9.0"}
        mock_response.raise_for_status = mocker.Mock()
        mock_response.status_code = 200

        mock_client = mocker.Mock()
        mock_client.get.return_value = mock_response
        mock_client.__enter__ = mocker.Mock(return_value=mock_client)
        mock_client.__exit__ = mocker.Mock(return_value=False)

        mocker.patch("httpx.Client", return_value=mock_client)

        result = _call_airflow_api("version", username="admin", password="admin")

        assert result == {"version": "2.9.0"}
        mock_client.get.assert_called_once()
        call_kwargs = mock_client.get.call_args[1]
        assert call_kwargs["auth"] == ("admin", "admin")

    def test_api_call_with_params(self, mocker):
        """Test API call with query parameters."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"dags": [], "total_entries": 0}
        mock_response.raise_for_status = mocker.Mock()
        mock_response.status_code = 200

        mock_client = mocker.Mock()
        mock_client.get.return_value = mock_response
        mock_client.__enter__ = mocker.Mock(return_value=mock_client)
        mock_client.__exit__ = mocker.Mock(return_value=False)

        mocker.patch("httpx.Client", return_value=mock_client)

        params = {"limit": 50, "offset": 10}
        result = _call_airflow_api("dags", params=params)

        assert result == {"dags": [], "total_entries": 0}
        mock_client.get.assert_called_once()
        call_kwargs = mock_client.get.call_args[1]
        assert call_kwargs["params"] == params

    def test_api_call_with_custom_url(self, mocker):
        """Test API call with custom Airflow URL."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"status": "ok"}
        mock_response.raise_for_status = mocker.Mock()
        mock_response.status_code = 200

        mock_client = mocker.Mock()
        mock_client.get.return_value = mock_response
        mock_client.__enter__ = mocker.Mock(return_value=mock_client)
        mock_client.__exit__ = mocker.Mock(return_value=False)

        mocker.patch("httpx.Client", return_value=mock_client)

        custom_url = "https://custom.airflow.com"
        result = _call_airflow_api("health", airflow_url=custom_url)

        assert result == {"status": "ok"}
        mock_client.get.assert_called_once()
        call_args = mock_client.get.call_args[0]
        assert call_args[0] == f"{custom_url}/api/v2/health"

    def test_api_call_request_exception(self, mocker):
        """Test API call handles request exceptions."""
        mock_client = mocker.Mock()
        mock_client.get.side_effect = httpx.RequestError("Connection failed")
        mock_client.__enter__ = mocker.Mock(return_value=mock_client)
        mock_client.__exit__ = mocker.Mock(return_value=False)

        mocker.patch("httpx.Client", return_value=mock_client)

        with pytest.raises(Exception) as exc_info:
            _call_airflow_api("dags")

        assert "Error connecting to Airflow API" in str(exc_info.value)

    def test_api_call_http_error(self, mocker):
        """Test API call handles HTTP errors."""
        mock_response = mocker.Mock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "404 Not Found",
            request=mocker.Mock(),
            response=mock_response,
        )

        mock_client = mocker.Mock()
        mock_client.get.return_value = mock_response
        mock_client.__enter__ = mocker.Mock(return_value=mock_client)
        mock_client.__exit__ = mocker.Mock(return_value=False)

        mocker.patch("httpx.Client", return_value=mock_client)

        with pytest.raises(Exception) as exc_info:
            _call_airflow_api("dags/nonexistent")

        assert "HTTP error from Airflow API" in str(exc_info.value)


class TestImplFunctions:
    """Tests for _impl functions using mocked API calls."""

    def test_get_dag_details_impl_success(self, mocker):
        """Test _get_dag_details_impl with successful response."""
        mock_dag_data = {
            "dag_id": "example_dag",
            "is_paused": False,
            "description": "Test DAG",
        }
        mocker.patch("astro_airflow_mcp.server._call_airflow_api", return_value=mock_dag_data)

        result = _get_dag_details_impl("example_dag")
        result_data = json.loads(result)

        assert result_data["dag_id"] == "example_dag"
        assert result_data["is_paused"] is False
        assert result_data["description"] == "Test DAG"

    def test_get_dag_details_impl_error(self, mocker):
        """Test _get_dag_details_impl with API error."""
        mocker.patch(
            "astro_airflow_mcp.server._call_airflow_api",
            side_effect=Exception("DAG not found"),
        )

        result = _get_dag_details_impl("nonexistent_dag")

        assert "DAG not found" in result

    def test_list_dags_impl_success(self, mocker):
        """Test _list_dags_impl with successful response."""
        mock_response = {
            "dags": [
                {"dag_id": "dag1", "is_paused": False},
                {"dag_id": "dag2", "is_paused": True},
            ],
            "total_entries": 2,
        }
        mocker.patch("astro_airflow_mcp.server._call_airflow_api", return_value=mock_response)

        result = _list_dags_impl(limit=10, offset=0)
        result_data = json.loads(result)

        assert result_data["total_dags"] == 2
        assert result_data["returned_count"] == 2
        assert len(result_data["dags"]) == 2
        assert result_data["dags"][0]["dag_id"] == "dag1"

    def test_list_dags_impl_empty(self, mocker):
        """Test _list_dags_impl with no DAGs."""
        mock_response = {"dags": [], "total_entries": 0}
        mocker.patch("astro_airflow_mcp.server._call_airflow_api", return_value=mock_response)

        result = _list_dags_impl()
        result_data = json.loads(result)

        assert result_data["total_dags"] == 0
        assert result_data["returned_count"] == 0
        assert result_data["dags"] == []


class TestConfiguration:
    """Tests for global configuration."""

    def test_configure_url(self):
        """Test configure() updates global URL."""
        from astro_airflow_mcp.server import _config

        original_url = _config.url
        try:
            configure(url="https://test.airflow.com")
            assert _config.url == "https://test.airflow.com"
        finally:
            # Restore original
            _config.url = original_url

    def test_configure_auth_token(self):
        """Test configure() updates global auth token."""
        from astro_airflow_mcp.server import _config

        original_token = _config.auth_token
        try:
            configure(auth_token="new_token_456")
            assert _config.auth_token == "new_token_456"
        finally:
            # Restore original
            _config.auth_token = original_token

    def test_configure_basic_auth(self):
        """Test configure() updates username and password."""
        from astro_airflow_mcp.server import _config

        original_username = _config.username
        original_password = _config.password
        try:
            configure(username="test_user", password="test_pass")
            assert _config.username == "test_user"
            assert _config.password == "test_pass"
        finally:
            # Restore originals
            _config.username = original_username
            _config.password = original_password

    def test_configure_all(self):
        """Test configure() updates all settings."""
        from astro_airflow_mcp.server import _config

        original_url = _config.url
        original_token = _config.auth_token
        original_username = _config.username
        original_password = _config.password
        try:
            configure(
                url="https://prod.airflow.com",
                auth_token="prod_token",
                username="prod_user",
                password="prod_pass",
            )
            assert _config.url == "https://prod.airflow.com"
            assert _config.auth_token == "prod_token"
            assert _config.username == "prod_user"
            assert _config.password == "prod_pass"
        finally:
            # Restore originals
            _config.url = original_url
            _config.auth_token = original_token
            _config.username = original_username
            _config.password = original_password

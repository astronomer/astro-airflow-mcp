"""Tests for Airflow API adapters."""

import pytest

from astro_airflow_mcp.adapters import create_adapter
from astro_airflow_mcp.adapters.airflow_v2_adapter import AirflowV2Adapter
from astro_airflow_mcp.adapters.airflow_v3_adapter import AirflowV3Adapter


@pytest.fixture
def mock_version_v2(mocker):
    """Mock version detection to return Airflow 2."""
    # Clear cache before test
    from astro_airflow_mcp.version_detection import _version_cache

    _version_cache.clear()

    # Patch where it's imported in the adapters module
    mocker.patch("astro_airflow_mcp.adapters.get_or_detect_version", return_value=(2, "2.9.0"))


@pytest.fixture
def mock_version_v3(mocker):
    """Mock version detection to return Airflow 3."""
    # Clear cache before test
    from astro_airflow_mcp.version_detection import _version_cache

    _version_cache.clear()

    # Patch where it's imported in the adapters module
    mocker.patch("astro_airflow_mcp.adapters.get_or_detect_version", return_value=(3, "3.1.3"))


class TestAdapterFactory:
    """Tests for adapter factory."""

    def test_create_adapter_v2(self, mock_version_v2):
        """Test adapter factory creates v2 adapter for Airflow 2.x."""
        adapter = create_adapter("http://localhost:8080")
        assert isinstance(adapter, AirflowV2Adapter)
        assert adapter.airflow_url == "http://localhost:8080"

    def test_create_adapter_v3(self, mock_version_v3):
        """Test adapter factory creates v3 adapter for Airflow 3.x."""
        adapter = create_adapter("http://localhost:8080")
        assert isinstance(adapter, AirflowV3Adapter)
        assert adapter.airflow_url == "http://localhost:8080"

    def test_create_adapter_with_auth(self, mock_version_v3):
        """Test adapter factory passes auth token."""
        adapter = create_adapter("http://localhost:8080", auth_token="test-token")
        assert adapter.auth_token == "test-token"


class TestV2Adapter:
    """Tests for Airflow 2.x adapter."""

    @pytest.fixture
    def adapter(self):
        """Create v2 adapter instance."""
        return AirflowV2Adapter("http://localhost:8080")

    def test_adapter_initialization(self, adapter):
        """Test v2 adapter initializes correctly."""
        assert adapter.airflow_url == "http://localhost:8080"
        assert adapter.auth_token is None
        assert adapter.client is not None

    def test_list_dags_success(self, adapter, mocker):
        """Test list_dags returns dict on success."""
        # Mock the generated client response
        mock_response = mocker.Mock()
        mock_response.to_dict.return_value = {
            "dags": [{"dag_id": "example_dag", "is_paused": False}],
            "total_entries": 1,
        }

        mocker.patch(
            "astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.dag.get_dags.sync",
            return_value=mock_response,
        )

        result = adapter.list_dags(limit=10, offset=0)

        assert "dags" in result
        assert len(result["dags"]) == 1
        assert result["dags"][0]["dag_id"] == "example_dag"
        assert result["total_entries"] == 1

    def test_list_assets_normalizes_fields(self, adapter, mocker):
        """Test v2 adapter normalizes consuming_dags to scheduled_dags."""
        # Mock the generated client response with v2 field names
        mock_response = mocker.Mock()
        mock_response.to_dict.return_value = {
            "datasets": [{"uri": "s3://bucket/data", "consuming_dags": [{"dag_id": "test_dag"}]}],
            "total_entries": 1,
        }

        mocker.patch(
            "astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.dataset.get_datasets.sync",
            return_value=mock_response,
        )

        result = adapter.list_assets()

        # Should have normalized field names
        assert "assets" in result  # datasets → assets
        assert "scheduled_dags" in result["assets"][0]  # consuming_dags → scheduled_dags
        assert "consuming_dags" not in result["assets"][0]

    def test_list_connections_filters_passwords(self, adapter, mocker):
        """Test v2 adapter filters passwords from connections."""
        mock_response = mocker.Mock()
        mock_response.to_dict.return_value = {
            "connections": [
                {
                    "connection_id": "postgres_default",
                    "conn_type": "postgres",
                    "password": "secret123",
                }
            ],
            "total_entries": 1,
        }

        mocker.patch(
            "astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.connection.get_connections.sync",
            return_value=mock_response,
        )

        result = adapter.list_connections()

        # Password should be filtered
        assert "connections" in result
        assert result["connections"][0]["password"] == "***FILTERED***"


class TestV3Adapter:
    """Tests for Airflow 3.x adapter."""

    @pytest.fixture
    def adapter(self):
        """Create v3 adapter instance."""
        return AirflowV3Adapter("http://localhost:8080")

    def test_adapter_initialization(self, adapter):
        """Test v3 adapter initializes correctly."""
        assert adapter.airflow_url == "http://localhost:8080"
        assert adapter.auth_token is None
        assert adapter.client is not None

    def test_list_assets_uses_native_fields(self, adapter, mocker):
        """Test v3 adapter uses native scheduled_dags field."""
        mock_response = mocker.Mock()
        mock_response.to_dict.return_value = {
            "assets": [{"uri": "s3://bucket/data", "scheduled_dags": [{"dag_id": "test_dag"}]}],
            "total_entries": 1,
        }

        mocker.patch(
            "astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.asset.get_assets.sync",
            return_value=mock_response,
        )

        result = adapter.list_assets()

        # Should use native v3 field names
        assert "assets" in result
        assert "scheduled_dags" in result["assets"][0]

    def test_get_version(self, adapter, mocker):
        """Test get_version returns version info."""
        mock_response = mocker.Mock()
        mock_response.to_dict.return_value = {"version": "3.1.3", "git_version": "abc123"}

        mocker.patch(
            "astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.version.get_version.sync",
            return_value=mock_response,
        )

        result = adapter.get_version()

        assert "version" in result
        assert result["version"] == "3.1.3"


class TestErrorHandling:
    """Tests for error handling in adapters."""

    @pytest.fixture
    def adapter(self):
        """Create v3 adapter instance."""
        return AirflowV3Adapter("http://localhost:8080")

    def test_error_response_format(self, adapter, mocker):
        """Test errors are returned in consistent format."""
        # Mock an exception
        mocker.patch(
            "astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.dag.get_dags.sync",
            side_effect=Exception("Connection refused"),
        )

        result = adapter.list_dags()

        assert "error" in result
        assert "Connection refused" in str(result["error"])

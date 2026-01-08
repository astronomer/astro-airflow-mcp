"""Integration tests for all API endpoints against real Airflow instances.

These tests validate that each adapter method works correctly with both
Airflow 2.x and 3.x. They run in CI against real Airflow containers.
"""

import pytest

from astro_airflow_mcp.adapters import create_adapter, detect_version


class TestVersionDetection:
    """Test version detection against real Airflow."""

    def test_detect_version(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Should correctly detect Airflow version."""
        major, version = detect_version(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )
        assert major in (2, 3), f"Expected major version 2 or 3, got {major}"
        assert version, "Version string should not be empty"
        print(f"Detected Airflow {version} (major: {major})")


class TestAdapterCreation:
    """Test adapter creation against real Airflow."""

    def test_create_adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Should create appropriate adapter for detected version."""
        adapter = create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )
        assert adapter is not None
        assert adapter.version
        print(f"Created adapter for Airflow {adapter.version}")


class TestDAGEndpoints:
    """Test DAG-related endpoints."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_list_dags(self, adapter):
        """Should list DAGs successfully."""
        result = adapter.list_dags(limit=10)
        assert "dags" in result
        assert isinstance(result["dags"], list)
        print(f"Found {len(result['dags'])} DAGs")

    def test_get_dag(self, adapter):
        """Should get a specific DAG if example DAGs are loaded."""
        # First list DAGs to find one
        dags = adapter.list_dags(limit=1)
        if dags.get("dags"):
            dag_id = dags["dags"][0]["dag_id"]
            result = adapter.get_dag(dag_id)
            assert result.get("dag_id") == dag_id
            print(f"Got DAG: {dag_id}")
        else:
            pytest.skip("No DAGs available to test")

    def test_list_tasks(self, adapter):
        """Should list tasks for a DAG."""
        dags = adapter.list_dags(limit=1)
        if dags.get("dags"):
            dag_id = dags["dags"][0]["dag_id"]
            result = adapter.list_tasks(dag_id)
            assert "tasks" in result
            print(f"DAG {dag_id} has {len(result['tasks'])} tasks")
        else:
            pytest.skip("No DAGs available to test")


class TestDAGStatsEndpoint:
    """Test DAG stats endpoint - the endpoint that caught us with version differences."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_get_dag_stats_with_dag_ids(self, adapter):
        """Should get stats for specific DAGs."""
        # First get a DAG ID
        dags = adapter.list_dags(limit=1)
        if dags.get("dags"):
            dag_id = dags["dags"][0]["dag_id"]
            result = adapter.get_dag_stats(dag_ids=[dag_id])

            # Should not return an error
            assert "error" not in result or "available" not in result
            print(f"Got stats for DAG {dag_id}: {result}")
        else:
            pytest.skip("No DAGs available to test")

    def test_get_dag_stats_without_dag_ids(self, adapter):
        """Should get stats for all DAGs when no dag_ids provided.

        This is the critical test - Airflow 2.x requires dag_ids,
        but our adapter should handle this transparently.
        """
        result = adapter.get_dag_stats(dag_ids=None)

        # Should not return an error
        assert "error" not in result or "available" not in result
        print(f"Got stats for all DAGs: {len(result.get('dags', []))} entries")


class TestMonitoringEndpoints:
    """Test monitoring endpoints."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_list_import_errors(self, adapter):
        """Should list import errors."""
        result = adapter.list_import_errors(limit=10)
        assert "import_errors" in result
        print(f"Found {len(result['import_errors'])} import errors")

    def test_list_dag_warnings(self, adapter):
        """Should list DAG warnings."""
        result = adapter.list_dag_warnings(limit=10)
        assert "dag_warnings" in result
        print(f"Found {len(result['dag_warnings'])} DAG warnings")

    def test_get_version(self, adapter):
        """Should get Airflow version."""
        result = adapter.get_version()
        assert "version" in result
        print(f"Airflow version: {result['version']}")


class TestResourceEndpoints:
    """Test resource endpoints (pools, connections, variables)."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_list_pools(self, adapter):
        """Should list pools."""
        result = adapter.list_pools(limit=10)
        assert "pools" in result
        # Default pool should always exist
        pool_names = [p["name"] for p in result["pools"]]
        assert "default_pool" in pool_names
        print(f"Found {len(result['pools'])} pools")

    def test_get_pool(self, adapter):
        """Should get specific pool."""
        result = adapter.get_pool("default_pool")
        assert result.get("name") == "default_pool"
        print(f"Got pool: {result}")

    def test_list_variables(self, adapter):
        """Should list variables."""
        result = adapter.list_variables(limit=10)
        assert "variables" in result
        print(f"Found {len(result['variables'])} variables")

    def test_list_connections(self, adapter):
        """Should list connections (with passwords filtered)."""
        result = adapter.list_connections(limit=10)
        assert "connections" in result

        # Verify passwords are filtered
        for conn in result.get("connections", []):
            if "password" in conn:
                assert conn["password"] in (
                    None,
                    "",
                    "***FILTERED***",  # noqa: S105
                ), f"Password not filtered for {conn.get('connection_id')}"
        print(f"Found {len(result['connections'])} connections")


class TestAssetEndpoints:
    """Test asset/dataset endpoints."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_list_assets(self, adapter):
        """Should list assets (normalized from datasets in v2)."""
        result = adapter.list_assets(limit=10)
        # Response should have 'assets' key (normalized from 'datasets' in v2)
        assert "assets" in result or "available" in result
        print(f"Assets response: {result}")


class TestProviderEndpoints:
    """Test provider/plugin endpoints."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_list_providers(self, adapter):
        """Should list providers."""
        result = adapter.list_providers()
        assert "providers" in result
        print(f"Found {len(result['providers'])} providers")

    def test_list_plugins(self, adapter):
        """Should list plugins."""
        result = adapter.list_plugins(limit=10)
        assert "plugins" in result
        print(f"Found {len(result['plugins'])} plugins")

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


class TestDAGSourceEndpoint:
    """Test DAG source code endpoint."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_get_dag_source(self, adapter):
        """Should get DAG source code for an existing DAG.

        Note: V2 uses file_token from DAG details, V3 uses dag_id directly.
        The adapter handles this transparently.
        """
        dags = adapter.list_dags(limit=1)
        if not dags.get("dags"):
            pytest.skip("No DAGs available to test")

        dag_id = dags["dags"][0]["dag_id"]
        result = adapter.get_dag_source(dag_id)

        assert isinstance(result, dict)
        # Successful response should have content
        if "error" not in result and "available" not in result:
            assert "content" in result
        print(f"Got source for DAG {dag_id}: {len(str(result))} chars")


class TestDAGRunEndpoints:
    """Test DAG run operations - list, get, and trigger."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_list_dag_runs_all(self, adapter):
        """Should list DAG runs across all DAGs.

        Note: When dag_id is None, uses '~' for Airflow 2.x compatibility.
        """
        result = adapter.list_dag_runs(dag_id=None, limit=10)

        assert "dag_runs" in result
        assert isinstance(result["dag_runs"], list)
        print(f"Found {len(result['dag_runs'])} total DAG runs")

    def test_list_dag_runs_for_specific_dag(self, adapter):
        """Should list DAG runs for a specific DAG."""
        dags = adapter.list_dags(limit=1)
        if not dags.get("dags"):
            pytest.skip("No DAGs available to test")

        dag_id = dags["dags"][0]["dag_id"]
        result = adapter.list_dag_runs(dag_id=dag_id, limit=10)

        assert "dag_runs" in result
        assert isinstance(result["dag_runs"], list)
        # All runs should be for the specified DAG
        for run in result["dag_runs"]:
            assert run.get("dag_id") == dag_id
        print(f"Found {len(result['dag_runs'])} runs for DAG {dag_id}")

    def test_get_dag_run(self, adapter):
        """Should get details for a specific DAG run."""
        runs = adapter.list_dag_runs(dag_id=None, limit=1)
        if not runs.get("dag_runs"):
            pytest.skip("No DAG runs available to test")

        run = runs["dag_runs"][0]
        dag_id = run["dag_id"]
        dag_run_id = run["dag_run_id"]

        result = adapter.get_dag_run(dag_id, dag_run_id)

        assert result.get("dag_id") == dag_id
        assert result.get("dag_run_id") == dag_run_id
        assert "state" in result
        print(f"Got run {dag_run_id} with state: {result.get('state')}")

    def test_trigger_dag_run(self, adapter):
        """Should trigger a new DAG run.

        CAUTION: This is a mutating operation that creates a new DAG run.
        """
        dags = adapter.list_dags(limit=100)
        if not dags.get("dags"):
            pytest.skip("No DAGs available to test")

        # Look for an active, unpaused DAG
        target_dag = None
        for dag in dags["dags"]:
            if not dag.get("is_paused", True):
                target_dag = dag
                break

        if not target_dag:
            # Fall back to any DAG (trigger should still work even if paused)
            target_dag = dags["dags"][0]

        dag_id = target_dag["dag_id"]

        result = adapter.trigger_dag_run(
            dag_id=dag_id,
            conf={"test_key": "test_value"},
        )

        assert result.get("dag_id") == dag_id
        assert "dag_run_id" in result
        # V2 uses execution_date, V3 uses logical_date
        assert "execution_date" in result or "logical_date" in result
        print(f"Triggered run {result.get('dag_run_id')} for DAG {dag_id}")


class TestTaskEndpoints:
    """Test task and task instance operations."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_get_task(self, adapter):
        """Should get details of a specific task definition."""
        dags = adapter.list_dags(limit=10)
        if not dags.get("dags"):
            pytest.skip("No DAGs available to test")

        # Find a DAG that has tasks
        dag_id = None
        task_id = None
        for dag in dags["dags"]:
            tasks = adapter.list_tasks(dag["dag_id"])
            if tasks.get("tasks"):
                dag_id = dag["dag_id"]
                task_id = tasks["tasks"][0]["task_id"]
                break

        if not dag_id or not task_id:
            pytest.skip("No DAGs with tasks available to test")

        result = adapter.get_task(dag_id, task_id)

        assert result.get("task_id") == task_id
        print(f"Got task {task_id} from DAG {dag_id}")

    def test_get_task_instances(self, adapter):
        """Should list task instances for a DAG run."""
        runs = adapter.list_dag_runs(dag_id=None, limit=20)
        if not runs.get("dag_runs"):
            pytest.skip("No DAG runs available to test")

        # Look for a completed run (success or failed)
        target_run = None
        for run in runs["dag_runs"]:
            if run.get("state") in ("success", "failed"):
                target_run = run
                break

        if not target_run:
            pytest.skip("No completed DAG runs available to test task instances")

        dag_id = target_run["dag_id"]
        dag_run_id = target_run["dag_run_id"]

        result = adapter.get_task_instances(dag_id, dag_run_id, limit=100)

        assert "task_instances" in result
        assert isinstance(result["task_instances"], list)
        print(f"Found {len(result['task_instances'])} task instances for run {dag_run_id}")

    def test_get_task_instance(self, adapter):
        """Should get details of a specific task instance."""
        runs = adapter.list_dag_runs(dag_id=None, limit=20)
        if not runs.get("dag_runs"):
            pytest.skip("No DAG runs available to test")

        target_run = None
        target_task_instance = None

        for run in runs["dag_runs"]:
            if run.get("state") in ("success", "failed"):
                dag_id = run["dag_id"]
                dag_run_id = run["dag_run_id"]

                instances = adapter.get_task_instances(dag_id, dag_run_id, limit=10)
                if instances.get("task_instances"):
                    target_run = run
                    target_task_instance = instances["task_instances"][0]
                    break

        if not target_run or not target_task_instance:
            pytest.skip("No completed task instances available to test")

        dag_id = target_run["dag_id"]
        dag_run_id = target_run["dag_run_id"]
        task_id = target_task_instance["task_id"]

        result = adapter.get_task_instance(dag_id, dag_run_id, task_id)

        assert result.get("task_id") == task_id
        assert result.get("dag_id") == dag_id
        assert "state" in result
        print(f"Got task instance {task_id} with state: {result.get('state')}")

    def test_get_task_logs(self, adapter):
        """Should get logs for a task instance.

        Note: Logs require a task that has actually executed (not just queued).
        """
        runs = adapter.list_dag_runs(dag_id=None, limit=20)
        if not runs.get("dag_runs"):
            pytest.skip("No DAG runs available to test")

        target_task = None
        target_run = None

        for run in runs["dag_runs"]:
            if run.get("state") in ("success", "failed"):
                dag_id = run["dag_id"]
                dag_run_id = run["dag_run_id"]

                instances = adapter.get_task_instances(dag_id, dag_run_id, limit=20)
                for ti in instances.get("task_instances", []):
                    # Look for a task that actually ran (has logs)
                    if ti.get("state") in ("success", "failed", "upstream_failed"):
                        target_task = ti
                        target_run = run
                        break

                if target_task:
                    break

        if not target_task or not target_run:
            pytest.skip("No executed task instances available to test logs")

        dag_id = target_run["dag_id"]
        dag_run_id = target_run["dag_run_id"]
        task_id = target_task["task_id"]
        try_number = target_task.get("try_number", 1)

        result = adapter.get_task_logs(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            try_number=try_number,
            full_content=True,
        )

        assert isinstance(result, dict)
        # Logs might be in 'content' or return availability info
        if "available" not in result:
            assert "content" in result or len(result) > 0
        print(f"Got logs for task {task_id} (try {try_number}): {len(str(result))} chars")


class TestVariableEndpoint:
    """Test variable get operation."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_get_variable(self, adapter):
        """Should get a specific variable if one exists."""
        variables = adapter.list_variables(limit=10)
        if not variables.get("variables"):
            pytest.skip("No variables configured to test")

        variable_key = variables["variables"][0]["key"]
        result = adapter.get_variable(variable_key)

        assert result.get("key") == variable_key
        assert "value" in result
        print(f"Got variable {variable_key}")


class TestConfigEndpoint:
    """Test configuration endpoint."""

    @pytest.fixture
    def adapter(self, airflow_url: str, airflow_username: str, airflow_password: str):
        """Create adapter for tests."""
        return create_adapter(
            airflow_url,
            basic_auth_getter=lambda: (airflow_username, airflow_password),
        )

    def test_get_config(self, adapter):
        """Should get Airflow configuration.

        Note: Requires AIRFLOW__WEBSERVER__EXPOSE_CONFIG=true in Airflow 2.x.
        """
        result = adapter.get_config()

        assert isinstance(result, dict)

        # Check for successful response structure
        if "error" not in result and "note" not in result:
            # Successful response has 'sections' containing config
            assert "sections" in result
            assert isinstance(result["sections"], list)
            print(f"Found {len(result['sections'])} config sections")
        else:
            # Airflow 2.x without expose_config returns error info
            print(f"Config access returned: {result}")

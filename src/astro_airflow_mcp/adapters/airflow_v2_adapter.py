"""Adapter for Airflow 2.x generated client."""

from typing import Any

from astro_airflow_mcp.adapters.base import AirflowAdapter
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.connection import get_connections

# Import v2 API functions
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.dag import (
    get_dag,
    get_dag_source,
    get_dags,
    get_task,
    get_tasks,
)
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.dag_run import (
    get_dag_run,
    get_dag_runs,
    post_dag_run,
)
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.dag_warning import get_dag_warnings
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.dataset import get_datasets
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.import_error import (
    get_import_errors,
)
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.monitoring import get_version
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.plugin import get_plugins
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.pool import get_pool, get_pools
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.provider import get_providers
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.task_instance import (
    get_task_instance,
)
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.api.variable import (
    get_variable,
    get_variables,
)

# Import v2 client
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.client import (
    AuthenticatedClient,
)
from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.models.error import Error


class AirflowV2Adapter(AirflowAdapter):
    """Adapter for Airflow 2.x API using generated client."""

    def __init__(
        self,
        airflow_url: str,
        auth_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ):
        super().__init__(airflow_url, auth_token, username, password)

        # Initialize the generated v2 client
        # Airflow 2.x uses /api/v1 as the base path
        headers = {}
        auth = None

        # Set up authentication - prefer basic auth for Airflow 2.x
        if username and password:
            # Use basic auth (typical for Airflow 2.x)
            auth = (username, password)
        elif auth_token:
            # Use Bearer token auth
            headers["Authorization"] = f"Bearer {auth_token}"

        # Get the underlying httpx client with auth
        # Important: base_url must include /api/v1 for Airflow 2.x
        import httpx

        base_url_with_api = f"{airflow_url}/api/v1"
        httpx_client = httpx.Client(
            base_url=base_url_with_api,
            headers=headers,
            auth=auth,
            timeout=30.0,
        )

        self.client = AuthenticatedClient(
            base_url=base_url_with_api,
            token="",
            headers=headers,
            timeout=httpx.Timeout(30.0),  # nosec B106
        )
        self.client.set_httpx_client(httpx_client)

    def list_dags(self, limit: int = 100, offset: int = 0, **kwargs) -> dict[str, Any]:
        """List all DAGs using v2 client."""
        try:
            result = get_dags.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, Error):
                return self._handle_error(result, "list_dags")
            if result is None:
                return {"dags": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_dags")

    def get_dag(self, dag_id: str) -> dict[str, Any]:
        """Get DAG details using v2 client."""
        try:
            result = get_dag.sync(dag_id=dag_id, client=self.client)
            if isinstance(result, Error):
                return self._handle_error(result, "get_dag")
            if result is None:
                return {"error": "DAG not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_dag")

    def get_dag_source(self, dag_id: str) -> dict[str, Any]:
        """Get source code of a DAG.

        Note: Airflow 2 requires a file_token, so we get DAG details first.
        """
        try:
            # First, get the DAG to get its file_token
            dag_result = get_dag.sync(dag_id=dag_id, client=self.client)
            if isinstance(dag_result, Error):
                return self._handle_error(dag_result, "get_dag_source")
            if dag_result is None:
                return {"error": "DAG not found"}

            dag_data = dag_result.to_dict()
            file_token = dag_data.get("file_token")
            if not file_token:
                return {"error": "DAG has no file_token"}

            # Now get the source using file_token
            result = get_dag_source.sync(file_token=file_token, client=self.client)
            if isinstance(result, Error):
                return self._handle_error(result, "get_dag_source")
            if result is None:
                return {"error": "DAG source not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_dag_source")

    def list_dag_runs(
        self, dag_id: str | None = None, limit: int = 100, offset: int = 0, **kwargs
    ) -> dict[str, Any]:
        """List DAG runs.

        Note: Airflow 2 requires dag_id. Use '~' to list runs for all DAGs.
        """
        try:
            # Airflow 2 requires dag_id, use '~' for all DAGs
            dag_id_param = dag_id if dag_id else "~"
            result = get_dag_runs.sync(
                dag_id=dag_id_param, client=self.client, limit=limit, offset=offset
            )

            if isinstance(result, Error):
                return self._handle_error(result, "list_dag_runs")
            if result is None:
                return {"dag_runs": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_dag_runs")

    def get_dag_run(self, dag_id: str, dag_run_id: str) -> dict[str, Any]:
        """Get details of a specific DAG run."""
        try:
            result = get_dag_run.sync(dag_id=dag_id, dag_run_id=dag_run_id, client=self.client)
            if isinstance(result, Error):
                return self._handle_error(result, "get_dag_run")
            if result is None:
                return {"error": "DAG run not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_dag_run")

    def trigger_dag(self, dag_id: str, conf: dict | None = None) -> dict[str, Any]:
        """Trigger a new DAG run."""
        try:
            from astro_airflow_mcp.clients.airflow_v2.airflow_v2_client.models.dag_run import DAGRun

            # Create DAG run body
            body = DAGRun()
            if conf:
                body.conf = conf  # type: ignore[assignment]

            result = post_dag_run.sync(dag_id=dag_id, client=self.client, body=body)
            if isinstance(result, Error):
                return self._handle_error(result, "trigger_dag")
            if result is None:
                return {"error": "Failed to trigger DAG"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "trigger_dag")

    def list_tasks(self, dag_id: str) -> dict[str, Any]:
        """List all tasks in a DAG."""
        try:
            result = get_tasks.sync(dag_id=dag_id, client=self.client)
            if isinstance(result, Error):
                return self._handle_error(result, "list_tasks")
            if result is None:
                return {"tasks": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_tasks")

    def get_task(self, dag_id: str, task_id: str) -> dict[str, Any]:
        """Get details of a specific task."""
        try:
            result = get_task.sync(dag_id=dag_id, task_id=task_id, client=self.client)
            if isinstance(result, Error):
                return self._handle_error(result, "get_task")
            if result is None:
                return {"error": "Task not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_task")

    def get_task_instance(self, dag_id: str, dag_run_id: str, task_id: str) -> dict[str, Any]:
        """Get details of a task instance."""
        try:
            result = get_task_instance.sync(
                dag_id=dag_id, dag_run_id=dag_run_id, task_id=task_id, client=self.client
            )
            if isinstance(result, Error):
                return self._handle_error(result, "get_task_instance")
            if result is None:
                return {"error": "Task instance not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_task_instance")

    def list_assets(self, limit: int = 100, offset: int = 0, **kwargs) -> dict[str, Any]:
        """List assets, normalizing field names for v2.

        Airflow 2.x uses 'datasets' endpoint and 'consuming_dags' field.
        We normalize to 'assets' and 'scheduled_dags' for consistency with v3 API.
        """
        try:
            result = get_datasets.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, Error):
                return self._handle_error(result, "list_assets")
            if result is None:
                return {"assets": [], "total_entries": 0}

            data = result.to_dict()

            # Normalize field names: datasets -> assets, consuming_dags -> scheduled_dags
            if "datasets" in data:
                data["assets"] = data.pop("datasets")

                # Normalize each asset's fields
                for asset in data.get("assets", []):
                    if "consuming_dags" in asset:
                        asset["scheduled_dags"] = asset.pop("consuming_dags")

            return data
        except Exception as e:
            return self._handle_error(e, "list_assets")

    def list_variables(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow variables."""
        try:
            result = get_variables.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, Error):
                return self._handle_error(result, "list_variables")
            if result is None:
                return {"variables": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_variables")

    def get_variable(self, variable_key: str) -> dict[str, Any]:
        """Get a specific variable."""
        try:
            result = get_variable.sync(variable_key=variable_key, client=self.client)
            if isinstance(result, Error):
                return self._handle_error(result, "get_variable")
            if result is None:
                return {"error": "Variable not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_variable")

    def list_connections(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow connections (passwords filtered)."""
        try:
            result = get_connections.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, Error):
                return self._handle_error(result, "list_connections")
            if result is None:
                return {"connections": [], "total_entries": 0}

            data = result.to_dict()

            # Filter out password fields for security
            if "connections" in data:
                for conn in data["connections"]:
                    if "password" in conn:
                        conn["password"] = "***FILTERED***"  # nosec B105

            return data
        except Exception as e:
            return self._handle_error(e, "list_connections")

    def list_pools(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow pools."""
        try:
            result = get_pools.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, Error):
                return self._handle_error(result, "list_pools")
            if result is None:
                return {"pools": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_pools")

    def get_version(self) -> dict[str, Any]:
        """Get Airflow version info."""
        try:
            result = get_version.sync(client=self.client)
            if isinstance(result, Error):
                return self._handle_error(result, "get_version")
            if result is None:
                return {"error": "Version info not available"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_version")

    def get_config(self) -> dict[str, Any]:
        """Get Airflow configuration.

        Note: Airflow 2.x always returns text/plain, not JSON.
        Using direct HTTP call to avoid JSON parsing errors.
        """
        try:
            # Use direct HTTP call - Airflow 2 config endpoint always returns text
            httpx_client = self.client.get_httpx_client()
            response = httpx_client.get("/config")
            response.raise_for_status()

            # Always return as text for Airflow 2
            return {"config": response.text}
        except Exception as e:
            return self._handle_error(e, "get_config")

    def get_pool(self, pool_name: str) -> dict[str, Any]:
        """Get details of a specific pool."""
        try:
            result = get_pool.sync(pool_name=pool_name, client=self.client)
            if isinstance(result, Error):
                return self._handle_error(result, "get_pool")
            if result is None:
                return {"error": "Pool not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_pool")

    def get_dag_stats(self) -> dict[str, Any]:
        """Get DAG run statistics by state.

        Note: This endpoint is only available in Airflow 3.x.
        """
        return {
            "error": "dagStats endpoint is not available in Airflow 2.x",
            "note": "This feature was added in Airflow 3.0",
            "alternative": "Use list_dag_runs to get DAG run information",
        }

    def list_dag_warnings(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List DAG warnings."""
        try:
            result = get_dag_warnings.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, Error):
                return self._handle_error(result, "list_dag_warnings")
            if result is None:
                return {"dag_warnings": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_dag_warnings")

    def list_import_errors(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List import errors from DAG files."""
        try:
            result = get_import_errors.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, Error):
                return self._handle_error(result, "list_import_errors")
            if result is None:
                return {"import_errors": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_import_errors")

    def list_plugins(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List installed Airflow plugins."""
        try:
            result = get_plugins.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, Error):
                return self._handle_error(result, "list_plugins")
            if result is None:
                return {"plugins": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_plugins")

    def list_providers(self) -> dict[str, Any]:
        """List installed Airflow provider packages."""
        try:
            result = get_providers.sync(client=self.client)
            if isinstance(result, Error):
                return self._handle_error(result, "list_providers")
            if result is None:
                return {"providers": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_providers")

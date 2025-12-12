"""Adapter for Airflow 3.x generated client."""

from typing import Any

from astro_airflow_mcp.adapters.base import AirflowAdapter
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.asset import get_assets
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.config import get_config
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.connection import get_connections

# Import v3 API functions
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.dag import (
    get_dag,
    get_dags,
)
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.dag_run import (
    get_dag_run,
    get_dag_runs,
    trigger_dag_run,
)
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.dag_source import get_dag_source
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.dag_stats import get_dag_stats
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.dag_warning import list_dag_warnings
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.import_error import (
    get_import_errors,
)
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.plugin import get_plugins
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.pool import get_pool, get_pools
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.provider import get_providers
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.task import get_task, get_tasks
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.task_instance import (
    get_task_instance,
)
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.variable import (
    get_variable,
    get_variables,
)
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.api.version import get_version

# Import v3 client
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.client import (
    AuthenticatedClient,
)
from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.models.http_validation_error import (
    HTTPValidationError,
)


class AirflowV3Adapter(AirflowAdapter):
    """Adapter for Airflow 3.x API using generated client."""

    def __init__(
        self,
        airflow_url: str,
        auth_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ):
        super().__init__(airflow_url, auth_token, username, password)

        # Initialize the generated v3 client
        # Airflow 3.x uses /api/v2 as the base path
        headers = {}
        auth = None

        # Set up authentication - Airflow 3.x can use either method
        if username and password:
            # Use basic auth
            auth = (username, password)
        elif auth_token:
            # Use Bearer token auth
            headers["Authorization"] = f"Bearer {auth_token}"

        # Get the underlying httpx client with auth
        # Note: base_url should NOT include /api/v2 because the generated
        # client paths already include it (e.g., "/api/v2/dags")
        import httpx

        httpx_client = httpx.Client(
            base_url=airflow_url,
            headers=headers,
            auth=auth,
            timeout=30.0,
        )

        self.client = AuthenticatedClient(
            base_url=airflow_url,
            token="",
            headers=headers,
            timeout=httpx.Timeout(30.0),  # nosec B106
        )
        self.client.set_httpx_client(httpx_client)

    def list_dags(self, limit: int = 100, offset: int = 0, **kwargs) -> dict[str, Any]:
        """List all DAGs using v3 client."""
        try:
            result = get_dags.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "list_dags")
            if result is None:
                return {"dags": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_dags")

    def get_dag(self, dag_id: str) -> dict[str, Any]:
        """Get DAG details using v3 client."""
        try:
            result = get_dag.sync(dag_id=dag_id, client=self.client)
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "get_dag")
            if result is None:
                return {"error": "DAG not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_dag")

    def get_dag_source(self, dag_id: str) -> dict[str, Any]:
        """Get source code of a DAG."""
        try:
            result = get_dag_source.sync(dag_id=dag_id, client=self.client)
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "get_dag_source")
            if result is None:
                return {"error": "DAG source not found"}
            # get_dag_source might return a string directly
            if isinstance(result, str):
                return {"content": result}
            return result.to_dict() if hasattr(result, "to_dict") else {"content": str(result)}
        except Exception as e:
            return self._handle_error(e, "get_dag_source")

    def list_dag_runs(
        self, dag_id: str | None = None, limit: int = 100, offset: int = 0, **kwargs
    ) -> dict[str, Any]:
        """List DAG runs.

        Note: Airflow 3.x also requires dag_id. Use '~' to list runs for all DAGs.
        """
        try:
            # Airflow 3 also requires dag_id, use '~' for all DAGs
            dag_id_param = dag_id if dag_id else "~"
            result = get_dag_runs.sync(
                dag_id=dag_id_param, client=self.client, limit=limit, offset=offset
            )

            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "get_dag_run")
            if result is None:
                return {"error": "DAG run not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_dag_run")

    def trigger_dag(self, dag_id: str, conf: dict | None = None) -> dict[str, Any]:
        """Trigger a new DAG run."""
        try:
            from astro_airflow_mcp.clients.airflow_v3.airflow_v3_client.models.dag_run_body import (
                DAGRunBody,
            )

            # Create DAG run body
            body = DAGRunBody()
            if conf:
                body.conf = conf

            result = trigger_dag_run.sync(dag_id=dag_id, client=self.client, body=body)
            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "get_task_instance")
            if result is None:
                return {"error": "Task instance not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_task_instance")

    def list_assets(self, limit: int = 100, offset: int = 0, **kwargs) -> dict[str, Any]:
        """List assets using v3 client (uses scheduled_dags natively)."""
        try:
            result = get_assets.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "list_assets")
            if result is None:
                return {"assets": [], "total_entries": 0}
            # v3 already uses 'assets' and 'scheduled_dags', no normalization needed
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_assets")

    def list_variables(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow variables."""
        try:
            result = get_variables.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "get_version")
            if result is None:
                return {"error": "Version info not available"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_version")

    def get_config(self) -> dict[str, Any]:
        """Get Airflow configuration."""
        try:
            result = get_config.sync(client=self.client)
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "get_config")
            if result is None:
                return {"error": "Configuration not available"}
            # Config might return text or structured data, handle both
            if hasattr(result, "to_dict"):
                return result.to_dict()
            else:
                return {"config": str(result)}
        except Exception as e:
            return self._handle_error(e, "get_config")

    def get_pool(self, pool_name: str) -> dict[str, Any]:
        """Get details of a specific pool."""
        try:
            result = get_pool.sync(pool_name=pool_name, client=self.client)
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "get_pool")
            if result is None:
                return {"error": "Pool not found"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_pool")

    def get_dag_stats(self) -> dict[str, Any]:
        """Get DAG run statistics by state."""
        try:
            result = get_dag_stats.sync(client=self.client)
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "get_dag_stats")
            if result is None:
                return {"error": "DAG stats not available"}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "get_dag_stats")

    def list_dag_warnings(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List DAG warnings."""
        try:
            result = list_dag_warnings.sync(client=self.client, limit=limit, offset=offset)
            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
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
            if isinstance(result, HTTPValidationError):
                return self._handle_error(result, "list_providers")
            if result is None:
                return {"providers": [], "total_entries": 0}
            return result.to_dict()
        except Exception as e:
            return self._handle_error(e, "list_providers")

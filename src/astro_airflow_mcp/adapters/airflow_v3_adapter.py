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

    @property
    def error_type(self) -> type:
        """Error type for Airflow 3.x API."""
        return HTTPValidationError

    @property
    def api_base_path(self) -> str:
        """API base path for Airflow 3.x."""
        return ""

    def _get_authenticated_client_class(self) -> type:
        """Get AuthenticatedClient class for v3."""
        return AuthenticatedClient

    def list_dags(self, limit: int = 100, offset: int = 0, **kwargs) -> dict[str, Any]:
        """List all DAGs using v3 client."""
        return self._execute(
            get_dags.sync,
            "list_dags",
            empty_result={"dags": [], "total_entries": 0},
            limit=limit,
            offset=offset,
        )

    def get_dag(self, dag_id: str) -> dict[str, Any]:
        """Get DAG details using v3 client."""
        return self._execute(
            get_dag.sync,
            "get_dag",
            empty_result={"error": "DAG not found"},
            dag_id=dag_id,
        )

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
        # Airflow 3 also requires dag_id, use '~' for all DAGs
        dag_id_param = dag_id if dag_id else "~"
        return self._execute(
            get_dag_runs.sync,
            "list_dag_runs",
            empty_result={"dag_runs": [], "total_entries": 0},
            dag_id=dag_id_param,
            limit=limit,
            offset=offset,
        )

    def get_dag_run(self, dag_id: str, dag_run_id: str) -> dict[str, Any]:
        """Get details of a specific DAG run."""
        return self._execute(
            get_dag_run.sync,
            "get_dag_run",
            empty_result={"error": "DAG run not found"},
            dag_id=dag_id,
            dag_run_id=dag_run_id,
        )

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
        return self._execute(
            get_tasks.sync,
            "list_tasks",
            empty_result={"tasks": [], "total_entries": 0},
            dag_id=dag_id,
        )

    def get_task(self, dag_id: str, task_id: str) -> dict[str, Any]:
        """Get details of a specific task."""
        return self._execute(
            get_task.sync,
            "get_task",
            empty_result={"error": "Task not found"},
            dag_id=dag_id,
            task_id=task_id,
        )

    def get_task_instance(self, dag_id: str, dag_run_id: str, task_id: str) -> dict[str, Any]:
        """Get details of a task instance."""
        return self._execute(
            get_task_instance.sync,
            "get_task_instance",
            empty_result={"error": "Task instance not found"},
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
        )

    def list_assets(self, limit: int = 100, offset: int = 0, **kwargs) -> dict[str, Any]:
        """List assets using v3 client (uses scheduled_dags natively)."""
        return self._execute(
            get_assets.sync,
            "list_assets",
            empty_result={"assets": [], "total_entries": 0},
            limit=limit,
            offset=offset,
        )

    def list_variables(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow variables."""
        return self._execute(
            get_variables.sync,
            "list_variables",
            empty_result={"variables": [], "total_entries": 0},
            limit=limit,
            offset=offset,
        )

    def get_variable(self, variable_key: str) -> dict[str, Any]:
        """Get a specific variable."""
        return self._execute(
            get_variable.sync,
            "get_variable",
            empty_result={"error": "Variable not found"},
            variable_key=variable_key,
        )

    def list_connections(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow connections (passwords filtered)."""
        result = self._execute(
            get_connections.sync,
            "list_connections",
            empty_result={"connections": [], "total_entries": 0},
            limit=limit,
            offset=offset,
        )
        return self._filter_passwords(result)

    def list_pools(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow pools."""
        return self._execute(
            get_pools.sync,
            "list_pools",
            empty_result={"pools": [], "total_entries": 0},
            limit=limit,
            offset=offset,
        )

    def get_version(self) -> dict[str, Any]:
        """Get Airflow version info."""
        return self._execute(
            get_version.sync,
            "get_version",
            empty_result={"error": "Version info not available"},
        )

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
        return self._execute(
            get_pool.sync,
            "get_pool",
            empty_result={"error": "Pool not found"},
            pool_name=pool_name,
        )

    def get_dag_stats(self) -> dict[str, Any]:
        """Get DAG run statistics by state."""
        return self._execute(
            get_dag_stats.sync,
            "get_dag_stats",
            empty_result={"error": "DAG stats not available"},
        )

    def list_dag_warnings(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List DAG warnings."""
        return self._execute(
            list_dag_warnings.sync,
            "list_dag_warnings",
            empty_result={"dag_warnings": [], "total_entries": 0},
            limit=limit,
            offset=offset,
        )

    def list_import_errors(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List import errors from DAG files."""
        return self._execute(
            get_import_errors.sync,
            "list_import_errors",
            empty_result={"import_errors": [], "total_entries": 0},
            limit=limit,
            offset=offset,
        )

    def list_plugins(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List installed Airflow plugins."""
        return self._execute(
            get_plugins.sync,
            "list_plugins",
            empty_result={"plugins": [], "total_entries": 0},
            limit=limit,
            offset=offset,
        )

    def list_providers(self) -> dict[str, Any]:
        """List installed Airflow provider packages."""
        return self._execute(
            get_providers.sync,
            "list_providers",
            empty_result={"providers": [], "total_entries": 0},
        )

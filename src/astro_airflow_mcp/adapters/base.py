"""Base adapter interface for Airflow API clients."""

from abc import ABC, abstractmethod
from typing import Any


class AirflowAdapter(ABC):
    """Abstract base class for Airflow API adapters.

    Adapters wrap version-specific generated clients and provide
    a consistent interface for the MCP server tools.
    """

    def __init__(
        self,
        airflow_url: str,
        auth_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ):
        """Initialize adapter with connection details.

        Args:
            airflow_url: Base URL of Airflow webserver
            auth_token: Optional Bearer token for authentication
            username: Optional username for basic auth
            password: Optional password for basic auth
        """
        self.airflow_url = airflow_url
        self.auth_token = auth_token
        self.username = username
        self.password = password

    # DAG Operations
    @abstractmethod
    def list_dags(self, limit: int = 100, offset: int = 0, **kwargs) -> dict[str, Any]:
        """List all DAGs."""
        pass

    @abstractmethod
    def get_dag(self, dag_id: str) -> dict[str, Any]:
        """Get details of a specific DAG."""
        pass

    @abstractmethod
    def get_dag_source(self, dag_id: str) -> dict[str, Any]:
        """Get source code of a DAG."""
        pass

    # DAG Run Operations
    @abstractmethod
    def list_dag_runs(
        self, dag_id: str | None = None, limit: int = 100, offset: int = 0, **kwargs
    ) -> dict[str, Any]:
        """List DAG runs."""
        pass

    @abstractmethod
    def get_dag_run(self, dag_id: str, dag_run_id: str) -> dict[str, Any]:
        """Get details of a specific DAG run."""
        pass

    @abstractmethod
    def trigger_dag(self, dag_id: str, conf: dict | None = None) -> dict[str, Any]:
        """Trigger a new DAG run."""
        pass

    # Task Operations
    @abstractmethod
    def list_tasks(self, dag_id: str) -> dict[str, Any]:
        """List all tasks in a DAG."""
        pass

    @abstractmethod
    def get_task(self, dag_id: str, task_id: str) -> dict[str, Any]:
        """Get details of a specific task."""
        pass

    @abstractmethod
    def get_task_instance(self, dag_id: str, dag_run_id: str, task_id: str) -> dict[str, Any]:
        """Get details of a task instance."""
        pass

    # Asset/Dataset Operations
    @abstractmethod
    def list_assets(self, limit: int = 100, offset: int = 0, **kwargs) -> dict[str, Any]:
        """List assets/datasets. Normalizes field names between versions."""
        pass

    # Variable Operations
    @abstractmethod
    def list_variables(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow variables."""
        pass

    @abstractmethod
    def get_variable(self, variable_key: str) -> dict[str, Any]:
        """Get a specific variable."""
        pass

    # Connection Operations
    @abstractmethod
    def list_connections(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow connections (passwords filtered)."""
        pass

    # Pool Operations
    @abstractmethod
    def list_pools(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow pools."""
        pass

    @abstractmethod
    def get_pool(self, pool_name: str) -> dict[str, Any]:
        """Get details of a specific pool."""
        pass

    # DAG Statistics and Warnings
    @abstractmethod
    def get_dag_stats(self) -> dict[str, Any]:
        """Get DAG run statistics by state."""
        pass

    @abstractmethod
    def list_dag_warnings(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List DAG warnings."""
        pass

    @abstractmethod
    def list_import_errors(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List import errors from DAG files."""
        pass

    # Plugin and Provider Operations
    @abstractmethod
    def list_plugins(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List installed Airflow plugins."""
        pass

    @abstractmethod
    def list_providers(self) -> dict[str, Any]:
        """List installed Airflow provider packages."""
        pass

    # System Operations
    @abstractmethod
    def get_version(self) -> dict[str, Any]:
        """Get Airflow version info."""
        pass

    @abstractmethod
    def get_config(self) -> dict[str, Any]:
        """Get Airflow configuration."""
        pass

    # Helper method for error handling
    def _handle_error(self, error: Any, operation: str) -> dict[str, Any]:
        """Convert errors to dict format.

        Args:
            error: Error object from generated client
            operation: Description of the operation that failed

        Returns:
            Dict with error information
        """
        error_msg = str(error)
        return {"error": error_msg, "operation": operation, "status": "failed"}

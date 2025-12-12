"""Base adapter interface for Airflow API clients."""

from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

import httpx


class AirflowAdapter(ABC):
    """Abstract base class for Airflow API adapters.

    Adapters wrap version-specific generated clients and provide
    a consistent interface for the MCP server tools. This base class
    provides common implementations for generated OpenAPI clients.
    """

    def __init__(
        self,
        airflow_url: str,
        auth_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ):
        """Initialize adapter with connection details and create client.

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
        self.client = self._create_client()

    @property
    @abstractmethod
    def error_type(self) -> type:
        """Error type for this API version.

        Returns:
            Error type class (e.g., Error for v2, HTTPValidationError for v3)
        """
        pass

    @property
    @abstractmethod
    def api_base_path(self) -> str:
        """API base path for this version.

        Returns:
            API path string (e.g., '/api/v1' for v2, '' for v3)
        """
        pass

    @abstractmethod
    def _get_authenticated_client_class(self) -> type:
        """Get the version-specific AuthenticatedClient class.

        Returns:
            AuthenticatedClient class for this version
        """
        pass

    def _create_client(self) -> Any:
        """Create and configure the generated client.

        Returns:
            Configured AuthenticatedClient instance
        """
        headers, auth = self._setup_auth()
        base_url = f"{self.airflow_url}{self.api_base_path}"

        # Create httpx client with auth
        httpx_client = httpx.Client(
            base_url=base_url,
            headers=headers,
            auth=auth,
            timeout=30.0,
        )

        # Create generated AuthenticatedClient
        AuthenticatedClientClass = self._get_authenticated_client_class()
        client = AuthenticatedClientClass(
            base_url=base_url,
            token="",  # nosec B106
            headers=headers,
            timeout=httpx.Timeout(30.0),
        )
        client.set_httpx_client(httpx_client)

        return client

    def _setup_auth(self) -> tuple[dict[str, str], tuple[str, str] | None]:
        """Set up authentication headers and credentials.

        Returns:
            Tuple of (headers dict, auth tuple or None)
        """
        headers: dict[str, str] = {}
        auth: tuple[str, str] | None = None

        if self.username and self.password:
            # Use basic auth (typical for Airflow 2.x)
            auth = (self.username, self.password)
        elif self.auth_token:
            # Use Bearer token auth
            headers["Authorization"] = f"Bearer {self.auth_token}"

        return headers, auth

    def _call_and_handle(
        self,
        client_func: Callable,
        operation_name: str,
        empty_result: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Common pattern for calling generated client and handling errors.

        Args:
            client_func: Generated client function to call
            operation_name: Name of operation for error messages
            empty_result: Dict to return if result is None
            **kwargs: Arguments to pass to client function

        Returns:
            Dict with operation result or error information
        """
        try:
            result = client_func(client=self.client, **kwargs)

            # Check for API error response
            if isinstance(result, self.error_type):
                return self._handle_error(result, operation_name)

            # Handle None result
            if result is None:
                return empty_result or {"error": f"{operation_name} not found"}

            # Convert to dict
            return result.to_dict()  # type: ignore[no-any-return]

        except Exception as e:
            return self._handle_error(e, operation_name)

    def _filter_passwords(self, data: dict[str, Any]) -> dict[str, Any]:
        """Filter password fields from connection data for security.

        Args:
            data: Dict containing connection data

        Returns:
            Dict with passwords filtered out
        """
        if "connections" in data:
            for conn in data["connections"]:
                if "password" in conn:
                    conn["password"] = "***FILTERED***"  # nosec B105

        return data  # type: ignore[no-any-return]

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

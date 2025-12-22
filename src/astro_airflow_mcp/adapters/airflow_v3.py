"""Adapter for Airflow 3.x API."""

from typing import Any

import httpx

from astro_airflow_mcp.adapters.base import AirflowAdapter, NotFoundError


class AirflowV3Adapter(AirflowAdapter):
    """Adapter for Airflow 3.x API (/api/v2).

    Airflow 3.x uses OAuth2 Password Bearer authentication:
    - If auth_token is provided, it's used directly as a Bearer token
    - If username/password are provided, the adapter exchanges them for a JWT
      via the /auth/token endpoint and uses the JWT for subsequent calls

    See: https://github.com/apache/airflow-client-python
    """

    def __init__(
        self,
        airflow_url: str,
        version: str,
        auth_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ):
        """Initialize Airflow 3 adapter with OAuth2 token support.

        Args:
            airflow_url: Base URL of Airflow webserver
            version: Full version string (e.g., "3.2.0")
            auth_token: Optional pre-obtained JWT token
            username: Optional username for OAuth2 token exchange
            password: Optional password for OAuth2 token exchange
        """
        # If username/password provided but no token, exchange for JWT
        if username and password and not auth_token:
            auth_token = self._exchange_for_token(airflow_url, username, password)

        # Call parent with the token (password auth now converted to JWT)
        super().__init__(airflow_url, version, auth_token=auth_token)

    @staticmethod
    def _exchange_for_token(airflow_url: str, username: str, password: str) -> str:
        """Exchange username/password for a JWT token via OAuth2 endpoint.

        Airflow 3 uses OAuth2 Password Bearer flow - POST credentials to
        /auth/token and receive a JWT access_token.

        Args:
            airflow_url: Base URL of Airflow webserver
            username: Airflow username
            password: Airflow password

        Returns:
            JWT access token string

        Raises:
            RuntimeError: If token exchange fails
        """
        token_url = f"{airflow_url}/auth/token"
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.post(
                    token_url,
                    data={"username": username, "password": password},
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                )
                response.raise_for_status()
                data = response.json()
                token = data.get("access_token")
                if not token:
                    raise RuntimeError(f"No access_token in response from {token_url}")
                return token
        except httpx.HTTPStatusError as e:
            raise RuntimeError(
                f"Failed to obtain JWT token from {token_url}: "
                f"{e.response.status_code} - {e.response.text}"
            ) from e
        except httpx.RequestError as e:
            raise RuntimeError(f"Failed to connect to {token_url}: {e}") from e

    @property
    def api_base_path(self) -> str:
        """API base path for Airflow 3.x."""
        return "/api/v2"

    def list_dags(self, limit: int = 100, offset: int = 0, **kwargs: Any) -> dict[str, Any]:
        """List all DAGs with optional filters.

        Args:
            limit: Maximum number of DAGs to return
            offset: Offset for pagination
            **kwargs: Additional filters (e.g., tags, paused, only_active)
                      Passed through to Airflow API for forward compatibility.
        """
        return self._call("dags", params={"limit": limit, "offset": offset}, **kwargs)

    def get_dag(self, dag_id: str) -> dict[str, Any]:
        """Get details of a specific DAG."""
        return self._call(f"dags/{dag_id}")

    def get_dag_source(self, dag_id: str) -> dict[str, Any]:
        """Get source code of a DAG.

        Note: Airflow 3 directly uses dag_id for source lookup.
        """
        return self._call(f"dagSources/{dag_id}")

    def list_dag_runs(
        self, dag_id: str | None = None, limit: int = 100, offset: int = 0, **kwargs: Any
    ) -> dict[str, Any]:
        """List DAG runs.

        Args:
            dag_id: Optional DAG ID. Use '~' or None for all DAGs.
            limit: Maximum number of runs to return
            offset: Offset for pagination
            **kwargs: Additional filters (e.g., state, start_date_gte)
        """
        dag_id_param = dag_id if dag_id else "~"
        return self._call(
            f"dags/{dag_id_param}/dagRuns",
            params={"limit": limit, "offset": offset},
            **kwargs,
        )

    def get_dag_run(self, dag_id: str, dag_run_id: str) -> dict[str, Any]:
        """Get details of a specific DAG run."""
        return self._call(f"dags/{dag_id}/dagRuns/{dag_run_id}")

    def list_tasks(self, dag_id: str) -> dict[str, Any]:
        """List all tasks in a DAG."""
        return self._call(f"dags/{dag_id}/tasks")

    def get_task(self, dag_id: str, task_id: str) -> dict[str, Any]:
        """Get details of a specific task."""
        return self._call(f"dags/{dag_id}/tasks/{task_id}")

    def get_task_instance(self, dag_id: str, dag_run_id: str, task_id: str) -> dict[str, Any]:
        """Get details of a task instance."""
        return self._call(f"dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}")

    def list_assets(self, limit: int = 100, offset: int = 0, **kwargs: Any) -> dict[str, Any]:
        """List assets (renamed from 'datasets' in Airflow 3)."""
        try:
            return self._call("assets", params={"limit": limit, "offset": offset}, **kwargs)
        except NotFoundError:
            return self._handle_not_found(
                "assets", alternative="Try 'datasets' endpoint if using older Airflow 3.x"
            )

    def list_variables(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow variables."""
        return self._call("variables", params={"limit": limit, "offset": offset})

    def get_variable(self, variable_key: str) -> dict[str, Any]:
        """Get a specific variable."""
        return self._call(f"variables/{variable_key}")

    def list_connections(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow connections (passwords filtered)."""
        data = self._call("connections", params={"limit": limit, "offset": offset})
        return self._filter_passwords(data)

    def list_pools(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List Airflow pools."""
        return self._call("pools", params={"limit": limit, "offset": offset})

    def get_pool(self, pool_name: str) -> dict[str, Any]:
        """Get details of a specific pool."""
        return self._call(f"pools/{pool_name}")

    def get_dag_stats(self, dag_ids: list[str] | None = None) -> dict[str, Any]:
        """Get DAG run statistics by state.

        Args:
            dag_ids: Optional list of DAG IDs to get stats for.
                     If None, returns stats for all DAGs.

        Note:
            Airflow 3.2.0 has bugs where:
            1. Calling without dag_ids causes a 500 error
            2. Multiple dag_ids in one call causes a 500 error
            3. DAGs with dag_display_name=None cause a 500 error

            We work around these by calling once per DAG and handling errors.

        Available in Airflow 3.0+. Returns counts by DAG and state.
        """
        try:
            # Workaround for Airflow 3.2.0 bugs
            if dag_ids:
                # Call once per DAG to avoid multiple dag_ids bug
                all_results: dict[str, Any] = {"dags": [], "total_entries": 0, "errors": []}
                for dag_id in dag_ids:
                    try:
                        result = self._call("dagStats", params={"dag_ids": dag_id})
                        all_results["dags"].extend(result.get("dags", []))
                        all_results["total_entries"] += result.get("total_entries", 0)
                    except Exception as e:
                        # Some DAGs may fail due to dag_display_name=None bug
                        all_results["errors"].append(
                            {
                                "dag_id": dag_id,
                                "error": str(e),
                                "note": "Airflow 3.2.0 bug: dag_display_name may be None",
                            }
                        )
                if not all_results["errors"]:
                    del all_results["errors"]
                return all_results
            else:
                # Pass empty dag_ids to avoid 500 error
                return self._call("dagStats", params={"dag_ids": ""})
        except NotFoundError:
            return self._handle_not_found(
                "dagStats", alternative="Use list_dag_runs to compute statistics"
            )

    def list_dag_warnings(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List DAG warnings."""
        return self._call("dagWarnings", params={"limit": limit, "offset": offset})

    def list_import_errors(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List import errors from DAG files."""
        return self._call("importErrors", params={"limit": limit, "offset": offset})

    def list_plugins(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List installed Airflow plugins."""
        return self._call("plugins", params={"limit": limit, "offset": offset})

    def list_providers(self) -> dict[str, Any]:
        """List installed Airflow provider packages."""
        return self._call("providers")

    def get_version(self) -> dict[str, Any]:
        """Get Airflow version info."""
        return self._call("version")

    def get_config(self) -> dict[str, Any]:
        """Get Airflow configuration."""
        return self._call("config")

    # Airflow 3.x specific features

    def get_task_instances(
        self, dag_id: str, dag_run_id: str, limit: int = 100, offset: int = 0
    ) -> dict[str, Any]:
        """List all task instances for a DAG run.

        Args:
            dag_id: DAG ID
            dag_run_id: DAG run ID
            limit: Maximum number of task instances to return
            offset: Offset for pagination

        Available in Airflow 3.0+.
        """
        try:
            return self._call(
                f"dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances",
                params={"limit": limit, "offset": offset},
            )
        except NotFoundError:
            return self._handle_not_found(f"dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances")

    def get_task_logs(
        self, dag_id: str, dag_run_id: str, task_id: str, try_number: int = 1
    ) -> dict[str, Any]:
        """Get logs for a specific task instance.

        Args:
            dag_id: DAG ID
            dag_run_id: DAG run ID
            task_id: Task ID
            try_number: Try number for the task (default 1)

        Available in Airflow 3.0+.
        """
        try:
            return self._call(
                f"dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{try_number}"
            )
        except NotFoundError:
            return self._handle_not_found(
                "task logs", alternative="Check if the task instance exists and has been executed"
            )

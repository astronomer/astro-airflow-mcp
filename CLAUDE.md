# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) server for Apache Airflow that enables AI assistants to interact with Airflow's REST API. The project uses FastMCP and supports two deployment modes:

1. **Standalone server**: Independent MCP server running on HTTP or stdio transport
2. **Airflow plugin**: Integrates directly into Airflow 3.x webserver via the plugin system

## Development Commands

### Setup
```bash
make setup              # Complete dev setup (install deps + hooks)
make install-dev        # Install with dev dependencies
make install-hooks      # Install pre-commit hooks only
```

### Running
```bash
make run               # Run MCP server (defaults to localhost:8000, connects to localhost:8080)
uv run pytest          # Run all tests
uv run pytest tests/test_server.py::test_name  # Run single test
```

### Code Quality
```bash
make check             # Run all checks (lint + type-check + security)
make lint              # Run ruff linting (reports only)
make format            # Auto-format code with ruff
make type-check        # Run mypy (excludes tests/)
make security          # Run bandit security checks (excludes tests/)
make pre-commit        # Run all pre-commit hooks
```

### Build & CI
```bash
make build             # Build wheel and sdist with uv
make test              # Run pytest
make ci                # Run full CI suite (pre-commit + tests)
make clean             # Remove build artifacts and cache
```

### Docker
```bash
make docker-build      # Build Docker image
make docker-run        # Run in container (exposes port 8000)
```

## Architecture

### Core Components

**`src/astro_airflow_mcp/server.py`** (1400+ lines)
- Main MCP server implementation using FastMCP
- All MCP tools are defined here with `@mcp.tool()` decorator
- Global `AirflowConfig` class holds connection settings (URL, auth token)
- `configure()` function sets global config used by all tools
- Each tool has an `_impl()` function for the core logic and a decorated wrapper that passes config
- Tools call `_call_airflow_api()` helper which handles requests and auth

**`src/astro_airflow_mcp/__main__.py`**
- CLI entry point (`astro-airflow-mcp` command)
- Parses args for transport (http/stdio), host, port, Airflow URL, auth token
- Calls `configure()` to set global connection settings
- Starts MCP server via `mcp.run()`

**`src/astro_airflow_mcp/plugin.py`**
- Airflow 3.x plugin integration
- Creates FastAPI app wrapping the MCP protocol app
- Mounts at `/mcp/v1` in Airflow webserver
- Uses `fastapi_apps` plugin hook to register with Airflow

**`src/astro_airflow_mcp/logging.py`**
- Custom logging setup for standalone mode
- Plugin mode uses Airflow's logging system

### MCP Tools Pattern

All tools follow this pattern:
1. User-facing `@mcp.tool()` decorated function (takes minimal params)
2. Calls `_impl()` function with config from global `_config` object
3. `_impl()` calls `_call_airflow_api()` with endpoint, params, auth
4. Returns JSON string (using `_wrap_list_response()` for paginated lists)

Example:
```python
@mcp.tool()
def get_dag_details(dag_id: str) -> str:
    """Docstring with usage guidance..."""
    return _get_dag_details_impl(
        dag_id=dag_id,
        airflow_url=_config.url,
        auth_token=_config.auth_token,
    )

def _get_dag_details_impl(dag_id: str, airflow_url: str, auth_token: str | None) -> str:
    data = _call_airflow_api(f"dags/{dag_id}", airflow_url, auth_token=auth_token)
    return json.dumps(data, indent=2)
```

### Key Airflow API Endpoints Used

The server wraps these Airflow REST API v2 endpoints:
- DAGs: `/api/v2/dags`, `/api/v2/dags/{dag_id}`, `/api/v2/dagSources/{dag_id}`, `/api/v2/dagStats`
- Tasks: `/api/v2/dags/{dag_id}/tasks`, `/api/v2/dags/{dag_id}/tasks/{task_id}`
- Task Instances: `/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}`
- DAG Runs: `/api/v2/dags/~/dagRuns`
- Warnings/Errors: `/api/v2/dagWarnings`, `/api/v2/importErrors`
- Pools: `/api/v2/pools`, `/api/v2/pools/{pool_name}`
- Variables: `/api/v2/variables`, `/api/v2/variables/{key}`
- Connections: `/api/v2/connections` (passwords filtered out)
- Assets: `/api/v2/assets`
- System: `/api/v2/version`, `/api/v2/config`, `/api/v2/plugins`, `/api/v2/providers`

## Testing

Tests are in `tests/` and use pytest with pytest-mock:
- `test_server.py`: Tests all MCP tools with mocked API responses
- `test_plugin.py`: Tests Airflow plugin loading
- `test_version.py`: Tests version retrieval

When writing tests:
- Mock `requests.get` to simulate Airflow API responses
- Test both success and error cases
- Verify returned JSON structure
- For list endpoints, include pagination metadata (`total_entries`)

## Configuration

**Standalone Mode (CLI)**:
- Command flags: `--airflow-url`, `--auth-token`, `--transport`, `--host`, `--port`
- Environment variables: `AIRFLOW_API_URL`, `AIRFLOW_AUTH_TOKEN`, `MCP_TRANSPORT`, `MCP_HOST`, `MCP_PORT`

**Plugin Mode**:
- Automatically uses the Airflow instance it's installed in
- No additional configuration needed
- Mounts at `/mcp/v1` endpoint on Airflow webserver

## Code Style & Quality

- Python 3.10+ required (uses `str | None` syntax)
- Line length: 100 characters
- Ruff for linting and formatting (config in `pyproject.toml`)
- Mypy for type checking (excludes tests/)
- Bandit for security checks (excludes tests/)
- Pre-commit hooks run all checks before commits

Key ruff rules enabled:
- E/W (pycodestyle)
- F (pyflakes)
- I (isort)
- B (flake8-bugbear)
- C4 (flake8-comprehensions)
- UP (pyupgrade)
- ARG (unused arguments)
- SIM (simplify)

## Package Management

- Uses `uv` for dependency management (fast, deterministic)
- Dependencies in `pyproject.toml` under `[project.dependencies]`
- Dev dependencies under `[tool.uv.dev-dependencies]`
- Optional plugin dependencies under `[project.optional-dependencies]`
- Lock file: `uv.lock`

## Entry Points

- CLI command: `astro-airflow-mcp` → `astro_airflow_mcp.__main__:main`
- Airflow plugin: `airflow_mcp` → `astro_airflow_mcp.plugin:AirflowMCPPlugin`

## Local Testing with Astro CLI

The default configuration works out-of-the-box with Astro CLI:
```bash
astro dev start        # Starts Airflow at localhost:8080
make run               # MCP server auto-connects to localhost:8080
```

## Important Implementation Notes

1. **Security**: The `list_connections` tool explicitly filters out password fields to prevent credential exposure via MCP

2. **Error Handling**: All `_impl()` functions wrap API calls in try-except and return error strings on failure

3. **Pagination**: List endpoints support `limit` and `offset` params (defaults: 100, 0) and return metadata via `_wrap_list_response()`

4. **Dual Mode Design**: Core server logic is transport-agnostic. Same MCP tools work in both standalone (HTTP/stdio) and plugin (FastAPI mount) modes

5. **Plugin Lifecycle**: The plugin uses FastAPI's lifespan context manager from the MCP app to properly initialize FastMCP's task group

6. **Import Errors**: The new `list_import_errors` endpoint helps debug DAG files that fail to parse/load

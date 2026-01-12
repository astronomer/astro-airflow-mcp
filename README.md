# Airflow MCP Server

[![CI](https://github.com/astronomer/astro-airflow-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/astronomer/astro-airflow-mcp/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyPI - Version](https://img.shields.io/pypi/v/astro-airflow-mcp.svg?color=blue)](https://pypi.org/project/astro-airflow-mcp)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://github.com/astronomer/astro-airflow-mcp/blob/main/LICENSE)

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server for Apache Airflow that provides AI assistants (like Claude, Cursor, etc.) with access to Airflow's REST API. Built with [FastMCP](https://github.com/jlowin/fastmcp).

## Features

- **Airflow 2.x and 3.x Support**: Automatic version detection with adapter pattern
- **MCP Tools** for accessing Airflow data:
  - DAG management (list, get details, get source code, stats, warnings, import errors, trigger, pause/unpause)
  - Task management (list, get details, get task instances, get logs)
  - Pool management (list, get details)
  - Variable management (list, get specific variables)
  - Connection management (list connections with credentials excluded)
  - Asset/Dataset management (unified naming across versions, data lineage)
  - Plugin and provider information
  - Configuration and version details
- **Consolidated Tools** for agent workflows:
  - `explore_dag`: Get comprehensive DAG information in one call
  - `diagnose_dag_run`: Debug failed DAG runs with task instance details
  - `get_system_health`: System overview with health, errors, and warnings
- **MCP Resources**: Static Airflow info exposed as resources (version, providers, plugins, config)
- **MCP Prompts**: Guided workflows for common tasks (troubleshooting, health checks, onboarding)
- **Dual deployment modes**:
  - **Standalone server**: Run as an independent MCP server
  - **Airflow plugin**: Integrate directly into Airflow 3.x webserver
- **Flexible Authentication**:
  - Bearer token (Airflow 2.x and 3.x)
  - Username/password with automatic OAuth2 token exchange (Airflow 3.x)
  - Basic auth (Airflow 2.x)


## Installation

We recommend installing astro-airflow-mcp with [uv](https://docs.astral.sh/uv/):

```bash
uv pip install astro-airflow-mcp
```

If installing into an Astro project as an Airflow plugin, add the package to your `requirements.txt`:

```bash
echo astro-airflow-mcp >> requirements.txt
```

## Usage

### Running the Server

After installation, start the MCP server:

```bash
astro-airflow-mcp
```

By default, this will:
- Run in **stdio mode** for use with MCP clients like Claude Desktop and Cursor
- Connect to Airflow at `http://localhost:8080` (default for `astro dev start`)

The server provides a set of tools that AI assistants can use to interact with your Airflow instance through the REST API. No authentication is required by default, but you can configure it using environment variables or command-line flags (see [Configuration](#configuration)).

**Stdio mode (default)** - For MCP clients:

```bash
# Default - runs in stdio mode
astro-airflow-mcp

# Airflow 3.x with username/password (OAuth2 token exchange)
astro-airflow-mcp --airflow-url https://my-airflow.example.com --username admin --password admin

# Airflow 2.x or 3.x with bearer token
astro-airflow-mcp --airflow-url https://my-airflow.example.com --auth-token my_token
```

**HTTP mode** - For standalone server:

```bash
# Run as HTTP server on localhost:8000
astro-airflow-mcp --transport http

# Customize host and port
astro-airflow-mcp --transport http --host 0.0.0.0 --port 9000
```

The HTTP mode exposes MCP protocol endpoints at `http://localhost:8000/mcp` and is useful for:
- Testing with HTTP-based MCP clients
- Running as a standalone service
- Docker deployments (see `make docker-run`)

### Using with MCP Clients

#### Claude Desktop

Claude Desktop uses stdio mode by default. Add to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "airflow": {
      "command": "astro-airflow-mcp",
      "env": {
        "AIRFLOW_API_URL": "http://your.airflow.domain.com",
        "AIRFLOW_USERNAME": "admin",
        "AIRFLOW_PASSWORD": "admin"
      }
    }
  }
}
```

Or with a bearer token:

```json
{
  "mcpServers": {
    "airflow": {
      "command": "astro-airflow-mcp",
      "env": {
        "AIRFLOW_API_URL": "http://your.airflow.domain.com",
        "AIRFLOW_AUTH_TOKEN": "your_token"
      }
    }
  }
}
```

#### Cursor

Configure in Cursor's MCP settings:

**Stdio mode (default)**:

```json
{
  "mcpServers": {
    "airflow": {
      "command": "astro-airflow-mcp",
      "args": [],
      "env": {
        "AIRFLOW_API_URL": "http://localhost:8080"
      }
    }
  }
}
```

**Or connect to a standalone HTTP server**:

```json
{
  "mcpServers": {
    "airflow": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

**Or connect to the Airflow plugin endpoint**:

```json
{
  "mcpServers": {
    "airflow": {
      "url": "http://localhost:8080/mcp/v1"
    }
  }
}
```

## Available Tools

### Consolidated Tools (Agent-Optimized)

| Tool | Description |
|------|-------------|
| `explore_dag` | Get comprehensive DAG info: metadata, tasks, recent runs, source code |
| `diagnose_dag_run` | Debug a DAG run: run details, failed task instances, logs |
| `get_system_health` | System overview: health status, import errors, warnings, DAG stats |

### Core Tools

| Tool | Description |
|------|-------------|
| `list_dags` | Get all DAGs and their metadata |
| `get_dag_details` | Get detailed info about a specific DAG |
| `get_dag_source` | Get the source code of a DAG |
| `get_dag_stats` | Get DAG run statistics (Airflow 3.x only) |
| `list_dag_warnings` | Get DAG import warnings |
| `list_import_errors` | Get import errors from DAG files that failed to parse |
| `list_dag_runs` | Get DAG run history |
| `get_dag_run` | Get specific DAG run details |
| `trigger_dag` | Trigger a new DAG run (start a workflow execution) |
| `pause_dag` | Pause a DAG to prevent new scheduled runs |
| `unpause_dag` | Unpause a DAG to resume scheduled runs |
| `list_tasks` | Get all tasks in a DAG |
| `get_task` | Get details about a specific task |
| `get_task_instance` | Get task instance execution details |
| `get_task_logs` | Get logs for a specific task instance execution |
| `list_pools` | Get all resource pools |
| `get_pool` | Get details about a specific pool |
| `list_variables` | Get all Airflow variables |
| `get_variable` | Get a specific variable by key |
| `list_connections` | Get all connections (credentials excluded for security) |
| `list_assets` | Get assets/datasets (unified naming across versions) |
| `list_plugins` | Get installed Airflow plugins |
| `list_providers` | Get installed provider packages |
| `get_airflow_config` | Get Airflow configuration |
| `get_airflow_version` | Get Airflow version information |
| `get_health` | Get Airflow health status |

### MCP Resources

| Resource URI | Description |
|--------------|-------------|
| `airflow://version` | Airflow version information |
| `airflow://providers` | Installed provider packages |
| `airflow://plugins` | Installed Airflow plugins |
| `airflow://config` | Airflow configuration |

### MCP Prompts

| Prompt | Description |
|--------|-------------|
| `troubleshoot_failed_dag` | Guided workflow for diagnosing DAG failures |
| `daily_health_check` | Morning health check routine |
| `onboard_new_dag` | Guide for understanding a new DAG |

## Development

### Quick Start

```bash
# Setup development environment
make setup

# Run tests
make test

# Run all checks
make check

# Run pre-commit hooks
make pre-commit
```

### Local Testing with Astro CLI

The easiest way to test the MCP server locally is with [Astro CLI](https://www.astronomer.io/docs/astro/cli/overview):

```bash
# Start a local Airflow instance with an astro project (optional but recommended)
astro dev start

# In another terminal, run the MCP server in HTTP mode for testing
# This uses HTTP mode explicitly for easier testing and debugging
make run
```

The `make run` command uses HTTP mode on `http://localhost:8000` which is useful for local testing. The default configuration connects to `http://localhost:8080` which matches Astro CLI's default Airflow webserver URL.

## Configuration

All tools use a global configuration that can be set via command-line flags or environment variables:

| Flag | Environment Variable | Default | Description |
|------|---------------------|---------|-------------|
| `--transport` | `MCP_TRANSPORT` | `stdio` | Transport mode (`stdio` or `http`) |
| `--host` | `MCP_HOST` | `localhost` | Host to bind to (HTTP mode only) |
| `--port` | `MCP_PORT` | `8000` | Port to bind to (HTTP mode only) |
| `--airflow-url` | `AIRFLOW_API_URL` | `http://localhost:8080` | Airflow webserver URL |
| `--auth-token` | `AIRFLOW_AUTH_TOKEN` | `None` | Bearer token for authentication |
| `--username` | `AIRFLOW_USERNAME` | `None` | Username for authentication (Airflow 3.x uses OAuth2 token exchange) |
| `--password` | `AIRFLOW_PASSWORD` | `None` | Password for authentication |

## Architecture

The server is built using [FastMCP](https://github.com/jlowin/fastmcp) with an adapter pattern for Airflow version compatibility:

### Core Components

- **Adapters** (`adapters/`): Version-specific API implementations
  - `AirflowAdapter` (base): Abstract interface for all Airflow API operations
  - `AirflowV2Adapter`: Airflow 2.x API (`/api/v1`) with basic auth
  - `AirflowV3Adapter`: Airflow 3.x API (`/api/v2`) with OAuth2 token exchange
- **Version Detection**: Automatic detection at startup by probing API endpoints
- **Models** (`models.py`): Pydantic models for type-safe API responses

### Version Handling Strategy

1. **Major versions (2.x vs 3.x)**: Adapter pattern with runtime version detection
2. **Minor versions (3.1 vs 3.2)**: Runtime feature detection with graceful fallbacks
3. **New API parameters**: Pass-through `**kwargs` for forward compatibility

### Deployment Modes

- **Standalone**: Independent ASGI application with HTTP/SSE transport
- **Plugin**: Mounted into Airflow 3.x FastAPI webserver

## Contributing

Contributions welcome! Please ensure:
- All tests pass (`make test`)
- Code passes linting (`make check`)
- Pre-commit hooks pass (`make pre-commit`)

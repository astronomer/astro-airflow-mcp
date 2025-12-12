#!/usr/bin/env bash
# Generate Python clients from OpenAPI specs for Airflow 2 and 3

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SPECS_DIR="$PROJECT_ROOT/openapi_specs"
CLIENTS_DIR="$PROJECT_ROOT/src/astro_airflow_mcp/clients"

echo "Generating Airflow API clients..."

# Clean existing generated clients
rm -rf "$CLIENTS_DIR/airflow_v2"
rm -rf "$CLIENTS_DIR/airflow_v3"

# Generate Airflow 2.9.0 client
echo "Generating Airflow 2.9.0 client..."
uv run openapi-python-client generate \
  --path "$SPECS_DIR/airflow-2.9.0-spec.yaml" \
  --output-path "$CLIENTS_DIR/airflow_v2" \
  --config "$SCRIPT_DIR/openapi-config-v2.yaml"

# Generate Airflow 3.1.3 client
echo "Generating Airflow 3.1.3 client..."
uv run openapi-python-client generate \
  --path "$SPECS_DIR/airflow-3.1.3-spec.yaml" \
  --output-path "$CLIENTS_DIR/airflow_v3" \
  --config "$SCRIPT_DIR/openapi-config-v3.yaml"

echo "Client generation complete!"
echo ""
echo "Generated clients:"
echo "  - src/astro_airflow_mcp/clients/airflow_v2/"
echo "  - src/astro_airflow_mcp/clients/airflow_v3/"

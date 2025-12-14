#!/usr/bin/env bash
# Generate Python clients from OpenAPI specs for Airflow 2 and 3

set -e

# Accept version numbers as arguments (defaults for backward compatibility)
AIRFLOW_V2_VERSION="${1:-2.9.0}"
AIRFLOW_V3_VERSION="${2:-3.1.3}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SPECS_DIR="$PROJECT_ROOT/openapi_specs"
CLIENTS_DIR="$PROJECT_ROOT/src/astro_airflow_mcp/clients"

echo "Generating Airflow API clients..."
echo "  Airflow v2: $AIRFLOW_V2_VERSION"
echo "  Airflow v3: $AIRFLOW_V3_VERSION"

# Clean existing generated clients
rm -rf "$CLIENTS_DIR/airflow_v2"
rm -rf "$CLIENTS_DIR/airflow_v3"

# Generate Airflow v2 client
echo "Generating Airflow v2 client ($AIRFLOW_V2_VERSION)..."
uv run openapi-python-client generate \
  --path "$SPECS_DIR/airflow-$AIRFLOW_V2_VERSION-spec.yaml" \
  --output-path "$CLIENTS_DIR/airflow_v2" \
  --config "$SCRIPT_DIR/openapi-config-v2.yaml"

# Generate Airflow v3 client
echo "Generating Airflow v3 client ($AIRFLOW_V3_VERSION)..."
uv run openapi-python-client generate \
  --path "$SPECS_DIR/airflow-$AIRFLOW_V3_VERSION-spec.yaml" \
  --output-path "$CLIENTS_DIR/airflow_v3" \
  --config "$SCRIPT_DIR/openapi-config-v3.yaml"

echo "Client generation complete!"
echo ""
echo "Generated clients:"
echo "  - src/astro_airflow_mcp/clients/airflow_v2/"
echo "  - src/astro_airflow_mcp/clients/airflow_v3/"

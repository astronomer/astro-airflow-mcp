---
description: How to work with the Airflow adapter pattern for v2/v3 compatibility
triggers:
  - adapter
  - airflow api
  - v2 vs v3
  - version compatibility
  - add endpoint
---

# Airflow Adapter Pattern

This skill covers how to work with the adapter pattern that enables compatibility with both Airflow 2.x and 3.x.

## Overview

The adapter pattern abstracts Airflow API differences:

```
MCP Tool → _get_adapter() → AirflowV2Adapter or AirflowV3Adapter → Airflow API
```

Version is auto-detected at startup by probing `/api/v2/version` then `/api/v1/version`.

## Key Files

- `adapters/base.py` - Abstract interface all adapters implement
- `adapters/airflow_v2.py` - Airflow 2.x implementation (`/api/v1`)
- `adapters/airflow_v3.py` - Airflow 3.x implementation (`/api/v2`)

## Adding New Endpoints

See [api-differences.md](api-differences.md) for version differences.
See [patterns.md](patterns.md) for implementation patterns.

## Quick Reference

```python
# Get adapter (auto-detects version)
adapter = _get_adapter()

# Make API calls through adapter
dags = adapter.list_dags(limit=100)
dag = adapter.get_dag("my_dag")
run = adapter.trigger_dag_run("my_dag", conf={"key": "value"})
```

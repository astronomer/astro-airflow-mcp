---
description: Verify code works with both Airflow 2.x and 3.x
---

Check if code changes are compatible with both Airflow versions.

## Checklist

1. **API Paths**: V2 uses `/api/v1`, V3 uses `/api/v2`
   - All API calls should go through adapters, not direct HTTP

2. **Field Names**: Some fields differ between versions
   - `execution_date` (v2) vs `logical_date` (v3)
   - `datasets` (v2) vs `assets` (v3)
   - `consuming_dags` (v2) vs `scheduled_dags` (v3)

3. **Endpoint Availability**: Some endpoints only exist in one version
   - Use `try/except NotFoundError` with `_handle_not_found()`

4. **Authentication**: Different auth mechanisms
   - V2: Basic auth
   - V3: OAuth2/JWT tokens

## Verification Steps

1. Check adapter implementations handle differences:
   ```bash
   grep -n "execution_date\|logical_date" src/astro_airflow_mcp/adapters/*.py
   grep -n "datasets\|assets" src/astro_airflow_mcp/adapters/*.py
   ```

2. Run unit tests:
   ```bash
   make test
   ```

3. Run integration tests against both versions:
   ```bash
   make test-integration-v2
   make test-integration-v3
   ```

## Common Issues

- Hardcoded `/api/v1` or `/api/v2` paths outside adapters
- Missing field normalization in V2 adapter
- Not handling `NotFoundError` for v3-only endpoints

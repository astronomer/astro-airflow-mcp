---
description: Add a new method to both Airflow adapters
---

Add a new API method to both V2 and V3 adapters.

## Steps

1. Add abstract method to `adapters/base.py`:

```python
@abstractmethod
def new_method(self, param: str) -> dict[str, Any]:
    """Description of what this method does.

    Args:
        param: Description
    """
    pass
```

2. Implement in `adapters/airflow_v2.py`:

```python
def new_method(self, param: str) -> dict[str, Any]:
    """Description."""
    return self._call(f"endpoint/{param}")
```

3. Implement in `adapters/airflow_v3.py`:

```python
def new_method(self, param: str) -> dict[str, Any]:
    """Description."""
    return self._call(f"endpoint/{param}")
```

## Handling Version Differences

If API differs between versions:

```python
# V2 adapter
def list_assets(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
    """V2 uses 'datasets' endpoint."""
    data = self._call("datasets", params={"limit": limit, "offset": offset})
    # Normalize field names
    if "datasets" in data:
        data["assets"] = data.pop("datasets")
    return data

# V3 adapter
def list_assets(self, limit: int = 100, offset: int = 0) -> dict[str, Any]:
    """V3 uses 'assets' endpoint."""
    return self._call("assets", params={"limit": limit, "offset": offset})
```

## Error Handling

For endpoints that may not exist in older versions:

```python
def new_method(self, param: str) -> dict[str, Any]:
    try:
        return self._call(f"newEndpoint/{param}")
    except NotFoundError:
        return self._handle_not_found(
            "newEndpoint",
            alternative="Use alternativeMethod instead"
        )
```

## Common API Differences

| Feature | Airflow 2.x | Airflow 3.x |
|---------|-------------|-------------|
| API path | `/api/v1` | `/api/v2` |
| Assets | `datasets` | `assets` |
| DAG runs | `execution_date` | `logical_date` |

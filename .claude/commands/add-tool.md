---
description: Add a new MCP tool to the server
---

Add a new MCP tool to `src/astro_airflow_mcp/server.py`.

## Steps

1. Create internal `_impl` function that calls the adapter:

```python
def _new_tool_impl(param: str) -> str:
    """Internal implementation."""
    try:
        adapter = _get_adapter()
        data = adapter.new_method(param)
        return json.dumps(data, indent=2)
    except Exception as e:
        return str(e)
```

2. Create the MCP tool with descriptive docstring:

```python
@mcp.tool()
def new_tool(param: str) -> str:
    """One-line description of what this tool does.

    Use this tool when the user asks about:
    - "Example query 1"
    - "Example query 2"

    Returns information including:
    - field1: Description
    - field2: Description

    Args:
        param: Description of the parameter

    Returns:
        JSON with the response data
    """
    return _new_tool_impl(param=param)
```

3. If the tool needs a new adapter method, run `/add-adapter-method` first.

4. Add the tool to README.md in the appropriate tools table.

## Docstring Format

The docstring is critical for AI discovery. Include:
- Clear one-line summary
- "Use this tool when" section with example queries
- "Returns information including" with key fields
- Args with descriptions
- Returns description

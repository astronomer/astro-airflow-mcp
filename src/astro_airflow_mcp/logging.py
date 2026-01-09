"""Logging utilities for Airflow MCP."""

import functools
import logging
from collections.abc import Callable
from typing import Any, TypeVar

from rich.console import Console
from rich.logging import RichHandler

# Type variable for preserving function signatures in decorators
F = TypeVar("F", bound=Callable[..., Any])


def get_logger(name: str | None = None) -> logging.Logger:
    """Get a logger instance nested under the airflow_mcp namespace.

    Args:
        name: Optional name for the logger. If not provided, returns root airflow_mcp logger.
              Will be nested under 'airflow_mcp' (e.g., 'airflow_mcp.server')

    Returns:
        A logger instance

    Example:
        >>> logger = get_logger("server")
        >>> logger.info("Starting server")
    """
    if name:
        return logging.getLogger(f"airflow_mcp.{name}")
    return logging.getLogger("airflow_mcp")


def configure_logging(level: str | int = logging.INFO, stdio_mode: bool = False) -> None:
    """Configure logging for the airflow_mcp package.

    Sets up a console handler with a standard format. When running in stdio mode,
    logs are sent to stderr to avoid corrupting JSON-RPC messages on stdout.

    Args:
        level: Logging level (e.g., logging.INFO, logging.DEBUG, or "INFO", "DEBUG")
              Defaults to INFO.
        stdio_mode: If True, logs to stderr instead of stdout to avoid corrupting
                   JSON-RPC protocol messages. Defaults to False.

    Example:
        >>> configure_logging(level=logging.DEBUG)
        >>> configure_logging(level=logging.INFO, stdio_mode=True)  # For MCP stdio transport
    """
    # Convert string level to int if needed
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)

    # Get the root airflow_mcp logger
    logger = get_logger()
    logger.setLevel(level)

    # Remove any existing handlers to avoid duplicates
    logger.handlers.clear()

    # Use RichHandler for colored output matching FastMCP's style
    # stderr=True in stdio mode to avoid corrupting JSON-RPC messages on stdout
    console = Console(stderr=stdio_mode)
    handler = RichHandler(
        console=console,
        show_time=False,
        show_path=False,
        show_level=False,
        rich_tracebacks=False,
        markup=True,
    )
    handler.setLevel(level)
    # Format with colored level and colon to match uvicorn/FastMCP style
    handler.setFormatter(logging.Formatter("[green]%(levelname)s:[/green]     %(message)s"))

    # Add handler to logger
    logger.addHandler(handler)

    # Prevent propagation to root logger to avoid duplicate logs
    logger.propagate = False


def log_tool_call(func: F) -> F:
    """Decorator that logs MCP tool calls with their arguments.

    Logs the tool name and arguments at INFO level when a tool is invoked.
    Uses the module's logger for the decorated function.

    Args:
        func: The tool function to wrap

    Returns:
        Wrapped function that logs before executing

    Example:
        >>> @mcp.tool()
        >>> @log_tool_call
        >>> def get_dag_details(dag_id: str) -> str:
        ...     return _get_dag_details_impl(dag_id)
    """
    # Get logger based on the function's module
    logger = get_logger(func.__module__)

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Format arguments for logging
        arg_parts: list[str] = []
        if args:
            arg_parts.extend(repr(arg) for arg in args)
        if kwargs:
            arg_parts.extend(f"{k}={v!r}" for k, v in kwargs.items())
        args_str = f"({', '.join(arg_parts)})" if arg_parts else ""

        logger.info(f"Tool call: {func.__name__}{args_str}")
        return func(*args, **kwargs)

    return wrapper  # type: ignore[return-value]

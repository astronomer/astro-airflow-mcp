from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.task import Task
from ...types import Response


def _get_kwargs(
    dag_id: str,
    task_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dags/{dag_id}/tasks/{task_id}".format(
            dag_id=quote(str(dag_id), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Task | None:
    if response.status_code == 200:
        response_200 = Task.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Task]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Task]:
    """Get simplified representation of a task

    Args:
        dag_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Task]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Task | None:
    """Get simplified representation of a task

    Args:
        dag_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Task
    """

    return sync_detailed(
        dag_id=dag_id,
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Task]:
    """Get simplified representation of a task

    Args:
        dag_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Task]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Task | None:
    """Get simplified representation of a task

    Args:
        dag_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Task
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            task_id=task_id,
            client=client,
        )
    ).parsed

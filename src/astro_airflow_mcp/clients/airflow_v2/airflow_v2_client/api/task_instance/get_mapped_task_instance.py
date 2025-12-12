from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.task_instance import TaskInstance
from ...types import Response


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    map_index: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
            map_index=quote(str(map_index), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TaskInstance | None:
    if response.status_code == 200:
        response_200 = TaskInstance.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | TaskInstance]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    map_index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | TaskInstance]:
    """Get a mapped task instance

     Get details of a mapped task instance.

    *New in version 2.3.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaskInstance]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        map_index=map_index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    map_index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Error | TaskInstance | None:
    """Get a mapped task instance

     Get details of a mapped task instance.

    *New in version 2.3.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaskInstance
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        map_index=map_index,
        client=client,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    map_index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | TaskInstance]:
    """Get a mapped task instance

     Get details of a mapped task instance.

    *New in version 2.3.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaskInstance]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        map_index=map_index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    map_index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Error | TaskInstance | None:
    """Get a mapped task instance

     Get details of a mapped task instance.

    *New in version 2.3.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaskInstance
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            map_index=map_index,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.task_collection import TaskCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    *,
    order_by: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["order_by"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dags/{dag_id}/tasks".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TaskCollection | None:
    if response.status_code == 200:
        response_200 = TaskCollection.from_dict(response.json())

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
) -> Response[Error | TaskCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    order_by: str | Unset = UNSET,
) -> Response[Error | TaskCollection]:
    """Get tasks for DAG

    Args:
        dag_id (str):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaskCollection]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    order_by: str | Unset = UNSET,
) -> Error | TaskCollection | None:
    """Get tasks for DAG

    Args:
        dag_id (str):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaskCollection
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    order_by: str | Unset = UNSET,
) -> Response[Error | TaskCollection]:
    """Get tasks for DAG

    Args:
        dag_id (str):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaskCollection]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    order_by: str | Unset = UNSET,
) -> Error | TaskCollection | None:
    """Get tasks for DAG

    Args:
        dag_id (str):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaskCollection
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            order_by=order_by,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clear_task_instances import ClearTaskInstances
from ...models.error import Error
from ...models.task_instance_reference_collection import TaskInstanceReferenceCollection
from ...types import Response


def _get_kwargs(
    dag_id: str,
    *,
    body: ClearTaskInstances,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dags/{dag_id}/clearTaskInstances".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | TaskInstanceReferenceCollection | None:
    if response.status_code == 200:
        response_200 = TaskInstanceReferenceCollection.from_dict(response.json())

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
) -> Response[Error | TaskInstanceReferenceCollection]:
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
    body: ClearTaskInstances,
) -> Response[Error | TaskInstanceReferenceCollection]:
    """Clear a set of task instances

     Clears a set of task instances associated with the DAG for a specified date range.

    Args:
        dag_id (str):
        body (ClearTaskInstances):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaskInstanceReferenceCollection]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClearTaskInstances,
) -> Error | TaskInstanceReferenceCollection | None:
    """Clear a set of task instances

     Clears a set of task instances associated with the DAG for a specified date range.

    Args:
        dag_id (str):
        body (ClearTaskInstances):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaskInstanceReferenceCollection
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClearTaskInstances,
) -> Response[Error | TaskInstanceReferenceCollection]:
    """Clear a set of task instances

     Clears a set of task instances associated with the DAG for a specified date range.

    Args:
        dag_id (str):
        body (ClearTaskInstances):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaskInstanceReferenceCollection]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClearTaskInstances,
) -> Error | TaskInstanceReferenceCollection | None:
    """Clear a set of task instances

     Clears a set of task instances associated with the DAG for a specified date range.

    Args:
        dag_id (str):
        body (ClearTaskInstances):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaskInstanceReferenceCollection
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            body=body,
        )
    ).parsed

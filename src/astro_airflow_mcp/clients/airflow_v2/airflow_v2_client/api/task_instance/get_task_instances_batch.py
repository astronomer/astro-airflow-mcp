from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_task_instance_form import ListTaskInstanceForm
from ...models.task_instance_collection import TaskInstanceCollection
from ...types import Response


def _get_kwargs(
    *,
    body: ListTaskInstanceForm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dags/~/dagRuns/~/taskInstances/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | TaskInstanceCollection | None:
    if response.status_code == 200:
        response_200 = TaskInstanceCollection.from_dict(response.json())

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
) -> Response[Error | TaskInstanceCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListTaskInstanceForm,
) -> Response[Error | TaskInstanceCollection]:
    """List task instances (batch)

     List task instances from all DAGs and DAG runs.
    This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limits.

    Args:
        body (ListTaskInstanceForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaskInstanceCollection]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ListTaskInstanceForm,
) -> Error | TaskInstanceCollection | None:
    """List task instances (batch)

     List task instances from all DAGs and DAG runs.
    This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limits.

    Args:
        body (ListTaskInstanceForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaskInstanceCollection
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListTaskInstanceForm,
) -> Response[Error | TaskInstanceCollection]:
    """List task instances (batch)

     List task instances from all DAGs and DAG runs.
    This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limits.

    Args:
        body (ListTaskInstanceForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TaskInstanceCollection]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListTaskInstanceForm,
) -> Error | TaskInstanceCollection | None:
    """List task instances (batch)

     List task instances from all DAGs and DAG runs.
    This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limits.

    Args:
        body (ListTaskInstanceForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TaskInstanceCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

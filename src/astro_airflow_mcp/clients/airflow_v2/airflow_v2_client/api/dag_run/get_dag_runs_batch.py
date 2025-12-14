from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_run_collection import DAGRunCollection
from ...models.error import Error
from ...models.list_dag_runs_form import ListDagRunsForm
from ...types import Response


def _get_kwargs(
    *,
    body: ListDagRunsForm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dags/~/dagRuns/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGRunCollection | Error | None:
    if response.status_code == 200:
        response_200 = DAGRunCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DAGRunCollection | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListDagRunsForm,
) -> Response[DAGRunCollection | Error]:
    """List DAG runs (batch)

     This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limit.

    Args:
        body (ListDagRunsForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGRunCollection | Error]
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
    body: ListDagRunsForm,
) -> DAGRunCollection | Error | None:
    """List DAG runs (batch)

     This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limit.

    Args:
        body (ListDagRunsForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGRunCollection | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListDagRunsForm,
) -> Response[DAGRunCollection | Error]:
    """List DAG runs (batch)

     This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limit.

    Args:
        body (ListDagRunsForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGRunCollection | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListDagRunsForm,
) -> DAGRunCollection | Error | None:
    """List DAG runs (batch)

     This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limit.

    Args:
        body (ListDagRunsForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGRunCollection | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

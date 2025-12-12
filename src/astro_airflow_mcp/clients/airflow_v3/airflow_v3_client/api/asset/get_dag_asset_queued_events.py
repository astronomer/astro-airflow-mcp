from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.queued_event_collection_response import QueuedEventCollectionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    *,
    before: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_before: None | str | Unset
    if isinstance(before, Unset):
        json_before = UNSET
    else:
        json_before = before
    params["before"] = json_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/assets/queuedEvents".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | QueuedEventCollectionResponse | None:
    if response.status_code == 200:
        response_200 = QueuedEventCollectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = HTTPExceptionResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HTTPExceptionResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = HTTPExceptionResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPExceptionResponse | HTTPValidationError | QueuedEventCollectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    before: None | str | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | QueuedEventCollectionResponse]:
    """Get Dag Asset Queued Events

     Get queued asset events for a DAG.

    Args:
        dag_id (str):
        before (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | QueuedEventCollectionResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        before=before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    before: None | str | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | QueuedEventCollectionResponse | None:
    """Get Dag Asset Queued Events

     Get queued asset events for a DAG.

    Args:
        dag_id (str):
        before (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | QueuedEventCollectionResponse
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        before=before,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    before: None | str | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | QueuedEventCollectionResponse]:
    """Get Dag Asset Queued Events

     Get queued asset events for a DAG.

    Args:
        dag_id (str):
        before (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | QueuedEventCollectionResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        before=before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    before: None | str | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | QueuedEventCollectionResponse | None:
    """Get Dag Asset Queued Events

     Get queued asset events for a DAG.

    Args:
        dag_id (str):
        before (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | QueuedEventCollectionResponse
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            before=before,
        )
    ).parsed

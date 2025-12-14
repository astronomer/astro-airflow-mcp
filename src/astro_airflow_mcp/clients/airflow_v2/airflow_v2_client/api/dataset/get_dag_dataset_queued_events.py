import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.queued_event_collection import QueuedEventCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    *,
    before: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dags/{dag_id}/datasets/queuedEvent".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | QueuedEventCollection | None:
    if response.status_code == 200:
        response_200 = QueuedEventCollection.from_dict(response.json())

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
) -> Response[Error | QueuedEventCollection]:
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
    before: datetime.datetime | Unset = UNSET,
) -> Response[Error | QueuedEventCollection]:
    """Get queued Dataset events for a DAG.

     Get queued Dataset events for a DAG.

    *New in version 2.9.0*

    Args:
        dag_id (str):
        before (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | QueuedEventCollection]
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
    client: AuthenticatedClient | Client,
    before: datetime.datetime | Unset = UNSET,
) -> Error | QueuedEventCollection | None:
    """Get queued Dataset events for a DAG.

     Get queued Dataset events for a DAG.

    *New in version 2.9.0*

    Args:
        dag_id (str):
        before (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | QueuedEventCollection
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        before=before,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    before: datetime.datetime | Unset = UNSET,
) -> Response[Error | QueuedEventCollection]:
    """Get queued Dataset events for a DAG.

     Get queued Dataset events for a DAG.

    *New in version 2.9.0*

    Args:
        dag_id (str):
        before (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | QueuedEventCollection]
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
    client: AuthenticatedClient | Client,
    before: datetime.datetime | Unset = UNSET,
) -> Error | QueuedEventCollection | None:
    """Get queued Dataset events for a DAG.

     Get queued Dataset events for a DAG.

    *New in version 2.9.0*

    Args:
        dag_id (str):
        before (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | QueuedEventCollection
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            before=before,
        )
    ).parsed

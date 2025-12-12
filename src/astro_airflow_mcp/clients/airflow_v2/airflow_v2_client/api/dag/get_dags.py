from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_collection import DAGCollection
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    only_active: bool | Unset = True,
    paused: bool | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    dag_id_pattern: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["order_by"] = order_by

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    params["only_active"] = only_active

    params["paused"] = paused

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["dag_id_pattern"] = dag_id_pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dags",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DAGCollection | Error | None:
    if response.status_code == 200:
        response_200 = DAGCollection.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DAGCollection | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    only_active: bool | Unset = True,
    paused: bool | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    dag_id_pattern: str | Unset = UNSET,
) -> Response[DAGCollection | Error]:
    """List DAGs

     List DAGs in the database.
    `dag_id_pattern` can be set to match dags of a specific pattern

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        tags (list[str] | Unset):
        only_active (bool | Unset):  Default: True.
        paused (bool | Unset):
        fields (list[str] | Unset):
        dag_id_pattern (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGCollection | Error]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        tags=tags,
        only_active=only_active,
        paused=paused,
        fields=fields,
        dag_id_pattern=dag_id_pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    only_active: bool | Unset = True,
    paused: bool | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    dag_id_pattern: str | Unset = UNSET,
) -> DAGCollection | Error | None:
    """List DAGs

     List DAGs in the database.
    `dag_id_pattern` can be set to match dags of a specific pattern

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        tags (list[str] | Unset):
        only_active (bool | Unset):  Default: True.
        paused (bool | Unset):
        fields (list[str] | Unset):
        dag_id_pattern (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGCollection | Error
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
        tags=tags,
        only_active=only_active,
        paused=paused,
        fields=fields,
        dag_id_pattern=dag_id_pattern,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    only_active: bool | Unset = True,
    paused: bool | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    dag_id_pattern: str | Unset = UNSET,
) -> Response[DAGCollection | Error]:
    """List DAGs

     List DAGs in the database.
    `dag_id_pattern` can be set to match dags of a specific pattern

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        tags (list[str] | Unset):
        only_active (bool | Unset):  Default: True.
        paused (bool | Unset):
        fields (list[str] | Unset):
        dag_id_pattern (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGCollection | Error]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        tags=tags,
        only_active=only_active,
        paused=paused,
        fields=fields,
        dag_id_pattern=dag_id_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    only_active: bool | Unset = True,
    paused: bool | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    dag_id_pattern: str | Unset = UNSET,
) -> DAGCollection | Error | None:
    """List DAGs

     List DAGs in the database.
    `dag_id_pattern` can be set to match dags of a specific pattern

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        tags (list[str] | Unset):
        only_active (bool | Unset):  Default: True.
        paused (bool | Unset):
        fields (list[str] | Unset):
        dag_id_pattern (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGCollection | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
            tags=tags,
            only_active=only_active,
            paused=paused,
            fields=fields,
            dag_id_pattern=dag_id_pattern,
        )
    ).parsed

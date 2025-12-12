from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_tag_collection_response import DAGTagCollectionResponse
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    tag_name_pattern: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_order_by: list[str] | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["order_by"] = json_order_by

    json_tag_name_pattern: None | str | Unset
    if isinstance(tag_name_pattern, Unset):
        json_tag_name_pattern = UNSET
    else:
        json_tag_name_pattern = tag_name_pattern
    params["tag_name_pattern"] = json_tag_name_pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dagTags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGTagCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DAGTagCollectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = HTTPExceptionResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HTTPExceptionResponse.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DAGTagCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    tag_name_pattern: None | str | Unset = UNSET,
) -> Response[DAGTagCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dag Tags

     Get all DAG tags.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `name`
        tag_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGTagCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        tag_name_pattern=tag_name_pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    tag_name_pattern: None | str | Unset = UNSET,
) -> DAGTagCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dag Tags

     Get all DAG tags.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `name`
        tag_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGTagCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
        tag_name_pattern=tag_name_pattern,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    tag_name_pattern: None | str | Unset = UNSET,
) -> Response[DAGTagCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dag Tags

     Get all DAG tags.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `name`
        tag_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGTagCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        tag_name_pattern=tag_name_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    tag_name_pattern: None | str | Unset = UNSET,
) -> DAGTagCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dag Tags

     Get all DAG tags.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `name`
        tag_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGTagCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
            tag_name_pattern=tag_name_pattern,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.user import User
from ...models.user_collection_item import UserCollectionItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    body: User,
    update_mask: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_update_mask: list[str] | Unset = UNSET
    if not isinstance(update_mask, Unset):
        json_update_mask = update_mask

    params["update_mask"] = json_update_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/users/{username}".format(
            username=quote(str(username), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | UserCollectionItem | None:
    if response.status_code == 200:
        response_200 = UserCollectionItem.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | UserCollectionItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: User,
    update_mask: list[str] | Unset = UNSET,
) -> Response[Error | UserCollectionItem]:
    """Update a user

     Update fields for a user.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        username (str):
        update_mask (list[str] | Unset):
        body (User): A user object with sensitive data.

            *New in version 2.1.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UserCollectionItem]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
        update_mask=update_mask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: User,
    update_mask: list[str] | Unset = UNSET,
) -> Error | UserCollectionItem | None:
    """Update a user

     Update fields for a user.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        username (str):
        update_mask (list[str] | Unset):
        body (User): A user object with sensitive data.

            *New in version 2.1.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UserCollectionItem
    """

    return sync_detailed(
        username=username,
        client=client,
        body=body,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: User,
    update_mask: list[str] | Unset = UNSET,
) -> Response[Error | UserCollectionItem]:
    """Update a user

     Update fields for a user.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        username (str):
        update_mask (list[str] | Unset):
        body (User): A user object with sensitive data.

            *New in version 2.1.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UserCollectionItem]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: User,
    update_mask: list[str] | Unset = UNSET,
) -> Error | UserCollectionItem | None:
    """Update a user

     Update fields for a user.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        username (str):
        update_mask (list[str] | Unset):
        body (User): A user object with sensitive data.

            *New in version 2.1.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UserCollectionItem
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            body=body,
            update_mask=update_mask,
        )
    ).parsed

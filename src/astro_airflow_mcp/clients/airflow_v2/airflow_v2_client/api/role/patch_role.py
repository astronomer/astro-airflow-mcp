from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.role import Role
from ...types import UNSET, Response, Unset


def _get_kwargs(
    role_name: str,
    *,
    body: Role,
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
        "url": "/roles/{role_name}".format(
            role_name=quote(str(role_name), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Role | None:
    if response.status_code == 200:
        response_200 = Role.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Role]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Role,
    update_mask: list[str] | Unset = UNSET,
) -> Response[Error | Role]:
    """Update a role

     Update a role.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        role_name (str):
        update_mask (list[str] | Unset):
        body (Role): a role item.

            *New in version 2.1.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Role]
    """

    kwargs = _get_kwargs(
        role_name=role_name,
        body=body,
        update_mask=update_mask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Role,
    update_mask: list[str] | Unset = UNSET,
) -> Error | Role | None:
    """Update a role

     Update a role.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        role_name (str):
        update_mask (list[str] | Unset):
        body (Role): a role item.

            *New in version 2.1.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Role
    """

    return sync_detailed(
        role_name=role_name,
        client=client,
        body=body,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Role,
    update_mask: list[str] | Unset = UNSET,
) -> Response[Error | Role]:
    """Update a role

     Update a role.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        role_name (str):
        update_mask (list[str] | Unset):
        body (Role): a role item.

            *New in version 2.1.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Role]
    """

    kwargs = _get_kwargs(
        role_name=role_name,
        body=body,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Role,
    update_mask: list[str] | Unset = UNSET,
) -> Error | Role | None:
    """Update a role

     Update a role.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        role_name (str):
        update_mask (list[str] | Unset):
        body (Role): a role item.

            *New in version 2.1.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Role
    """

    return (
        await asyncio_detailed(
            role_name=role_name,
            client=client,
            body=body,
            update_mask=update_mask,
        )
    ).parsed

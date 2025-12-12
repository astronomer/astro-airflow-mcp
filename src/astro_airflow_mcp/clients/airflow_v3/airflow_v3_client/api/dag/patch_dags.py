from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_collection_response import DAGCollectionResponse
from ...models.dag_patch_body import DAGPatchBody
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.patch_dags_tags_match_mode_type_0 import PatchDagsTagsMatchModeType0
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DAGPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    tags: list[str] | Unset = UNSET,
    tags_match_mode: None | PatchDagsTagsMatchModeType0 | Unset = UNSET,
    owners: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    exclude_stale: bool | Unset = True,
    paused: bool | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_update_mask: list[str] | None | Unset
    if isinstance(update_mask, Unset):
        json_update_mask = UNSET
    elif isinstance(update_mask, list):
        json_update_mask = update_mask

    else:
        json_update_mask = update_mask
    params["update_mask"] = json_update_mask

    params["limit"] = limit

    params["offset"] = offset

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_tags_match_mode: None | str | Unset
    if isinstance(tags_match_mode, Unset):
        json_tags_match_mode = UNSET
    elif isinstance(tags_match_mode, PatchDagsTagsMatchModeType0):
        json_tags_match_mode = tags_match_mode.value
    else:
        json_tags_match_mode = tags_match_mode
    params["tags_match_mode"] = json_tags_match_mode

    json_owners: list[str] | Unset = UNSET
    if not isinstance(owners, Unset):
        json_owners = owners

    params["owners"] = json_owners

    json_dag_id_pattern: None | str | Unset
    if isinstance(dag_id_pattern, Unset):
        json_dag_id_pattern = UNSET
    else:
        json_dag_id_pattern = dag_id_pattern
    params["dag_id_pattern"] = json_dag_id_pattern

    params["exclude_stale"] = exclude_stale

    json_paused: bool | None | Unset
    if isinstance(paused, Unset):
        json_paused = UNSET
    else:
        json_paused = paused
    params["paused"] = json_paused

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/dags",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DAGCollectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = HTTPExceptionResponse.from_dict(response.json())

        return response_400

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
) -> Response[DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DAGPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    tags: list[str] | Unset = UNSET,
    tags_match_mode: None | PatchDagsTagsMatchModeType0 | Unset = UNSET,
    owners: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    exclude_stale: bool | Unset = True,
    paused: bool | None | Unset = UNSET,
) -> Response[DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Patch Dags

     Patch multiple DAGs.

    Args:
        update_mask (list[str] | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        tags (list[str] | Unset):
        tags_match_mode (None | PatchDagsTagsMatchModeType0 | Unset):
        owners (list[str] | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        exclude_stale (bool | Unset):  Default: True.
        paused (bool | None | Unset):
        body (DAGPatchBody): Dag Serializer for updatable bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        update_mask=update_mask,
        limit=limit,
        offset=offset,
        tags=tags,
        tags_match_mode=tags_match_mode,
        owners=owners,
        dag_id_pattern=dag_id_pattern,
        exclude_stale=exclude_stale,
        paused=paused,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DAGPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    tags: list[str] | Unset = UNSET,
    tags_match_mode: None | PatchDagsTagsMatchModeType0 | Unset = UNSET,
    owners: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    exclude_stale: bool | Unset = True,
    paused: bool | None | Unset = UNSET,
) -> DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Patch Dags

     Patch multiple DAGs.

    Args:
        update_mask (list[str] | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        tags (list[str] | Unset):
        tags_match_mode (None | PatchDagsTagsMatchModeType0 | Unset):
        owners (list[str] | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        exclude_stale (bool | Unset):  Default: True.
        paused (bool | None | Unset):
        body (DAGPatchBody): Dag Serializer for updatable bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        update_mask=update_mask,
        limit=limit,
        offset=offset,
        tags=tags,
        tags_match_mode=tags_match_mode,
        owners=owners,
        dag_id_pattern=dag_id_pattern,
        exclude_stale=exclude_stale,
        paused=paused,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DAGPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    tags: list[str] | Unset = UNSET,
    tags_match_mode: None | PatchDagsTagsMatchModeType0 | Unset = UNSET,
    owners: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    exclude_stale: bool | Unset = True,
    paused: bool | None | Unset = UNSET,
) -> Response[DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Patch Dags

     Patch multiple DAGs.

    Args:
        update_mask (list[str] | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        tags (list[str] | Unset):
        tags_match_mode (None | PatchDagsTagsMatchModeType0 | Unset):
        owners (list[str] | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        exclude_stale (bool | Unset):  Default: True.
        paused (bool | None | Unset):
        body (DAGPatchBody): Dag Serializer for updatable bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        update_mask=update_mask,
        limit=limit,
        offset=offset,
        tags=tags,
        tags_match_mode=tags_match_mode,
        owners=owners,
        dag_id_pattern=dag_id_pattern,
        exclude_stale=exclude_stale,
        paused=paused,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DAGPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    tags: list[str] | Unset = UNSET,
    tags_match_mode: None | PatchDagsTagsMatchModeType0 | Unset = UNSET,
    owners: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    exclude_stale: bool | Unset = True,
    paused: bool | None | Unset = UNSET,
) -> DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Patch Dags

     Patch multiple DAGs.

    Args:
        update_mask (list[str] | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        tags (list[str] | Unset):
        tags_match_mode (None | PatchDagsTagsMatchModeType0 | Unset):
        owners (list[str] | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        exclude_stale (bool | Unset):  Default: True.
        paused (bool | None | Unset):
        body (DAGPatchBody): Dag Serializer for updatable bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            update_mask=update_mask,
            limit=limit,
            offset=offset,
            tags=tags,
            tags_match_mode=tags_match_mode,
            owners=owners,
            dag_id_pattern=dag_id_pattern,
            exclude_stale=exclude_stale,
            paused=paused,
        )
    ).parsed

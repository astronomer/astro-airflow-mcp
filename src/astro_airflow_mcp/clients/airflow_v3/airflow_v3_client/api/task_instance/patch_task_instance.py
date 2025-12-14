from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.patch_task_instance_body import PatchTaskInstanceBody
from ...models.task_instance_collection_response import TaskInstanceCollectionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    body: PatchTaskInstanceBody,
    map_index: int | None | Unset = UNSET,
    update_mask: list[str] | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_map_index: int | None | Unset
    if isinstance(map_index, Unset):
        json_map_index = UNSET
    else:
        json_map_index = map_index
    params["map_index"] = json_map_index

    json_update_mask: list[str] | None | Unset
    if isinstance(update_mask, Unset):
        json_update_mask = UNSET
    elif isinstance(update_mask, list):
        json_update_mask = update_mask

    else:
        json_update_mask = update_mask
    params["update_mask"] = json_update_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse | None:
    if response.status_code == 200:
        response_200 = TaskInstanceCollectionResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = HTTPExceptionResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: PatchTaskInstanceBody,
    map_index: int | None | Unset = UNSET,
    update_mask: list[str] | None | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]:
    """Patch Task Instance

     Update a task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int | None | Unset):
        update_mask (list[str] | None | Unset):
        body (PatchTaskInstanceBody): Request body for Clear Task Instances endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        body=body,
        map_index=map_index,
        update_mask=update_mask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: PatchTaskInstanceBody,
    map_index: int | None | Unset = UNSET,
    update_mask: list[str] | None | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse | None:
    """Patch Task Instance

     Update a task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int | None | Unset):
        update_mask (list[str] | None | Unset):
        body (PatchTaskInstanceBody): Request body for Clear Task Instances endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        client=client,
        body=body,
        map_index=map_index,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: PatchTaskInstanceBody,
    map_index: int | None | Unset = UNSET,
    update_mask: list[str] | None | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]:
    """Patch Task Instance

     Update a task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int | None | Unset):
        update_mask (list[str] | None | Unset):
        body (PatchTaskInstanceBody): Request body for Clear Task Instances endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        body=body,
        map_index=map_index,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: PatchTaskInstanceBody,
    map_index: int | None | Unset = UNSET,
    update_mask: list[str] | None | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse | None:
    """Patch Task Instance

     Update a task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int | None | Unset):
        update_mask (list[str] | None | Unset):
        body (PatchTaskInstanceBody): Request body for Clear Task Instances endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            client=client,
            body=body,
            map_index=map_index,
            update_mask=update_mask,
        )
    ).parsed

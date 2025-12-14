from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_patch_body import DAGPatchBody
from ...models.dag_response import DAGResponse
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    *,
    body: DAGPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/dags/{dag_id}".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DAGResponse.from_dict(response.json())

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
) -> Response[DAGResponse | HTTPExceptionResponse | HTTPValidationError]:
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
    body: DAGPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
) -> Response[DAGResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Patch Dag

     Patch the specific DAG.

    Args:
        dag_id (str):
        update_mask (list[str] | None | Unset):
        body (DAGPatchBody): Dag Serializer for updatable bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        body=body,
        update_mask=update_mask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    body: DAGPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
) -> DAGResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Patch Dag

     Patch the specific DAG.

    Args:
        dag_id (str):
        update_mask (list[str] | None | Unset):
        body (DAGPatchBody): Dag Serializer for updatable bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        body=body,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    body: DAGPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
) -> Response[DAGResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Patch Dag

     Patch the specific DAG.

    Args:
        dag_id (str):
        update_mask (list[str] | None | Unset):
        body (DAGPatchBody): Dag Serializer for updatable bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        body=body,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    body: DAGPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
) -> DAGResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Patch Dag

     Patch the specific DAG.

    Args:
        dag_id (str):
        update_mask (list[str] | None | Unset):
        body (DAGPatchBody): Dag Serializer for updatable bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            body=body,
            update_mask=update_mask,
        )
    ).parsed

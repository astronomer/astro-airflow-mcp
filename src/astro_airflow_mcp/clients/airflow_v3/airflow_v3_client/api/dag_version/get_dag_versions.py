from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_version_collection_response import DAGVersionCollectionResponse
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    version_number: int | Unset = UNSET,
    bundle_name: str | Unset = UNSET,
    bundle_version: None | str | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["version_number"] = version_number

    params["bundle_name"] = bundle_name

    json_bundle_version: None | str | Unset
    if isinstance(bundle_version, Unset):
        json_bundle_version = UNSET
    else:
        json_bundle_version = bundle_version
    params["bundle_version"] = json_bundle_version

    json_order_by: list[str] | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["order_by"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagVersions".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGVersionCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DAGVersionCollectionResponse.from_dict(response.json())

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
) -> Response[DAGVersionCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
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
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    version_number: int | Unset = UNSET,
    bundle_name: str | Unset = UNSET,
    bundle_version: None | str | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
) -> Response[DAGVersionCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dag Versions

     Get all DAG Versions.

    This endpoint allows specifying `~` as the dag_id to retrieve DAG Versions for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        version_number (int | Unset):
        bundle_name (str | Unset):
        bundle_version (None | str | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, version_number,
            bundle_name, bundle_version`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGVersionCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        limit=limit,
        offset=offset,
        version_number=version_number,
        bundle_name=bundle_name,
        bundle_version=bundle_version,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    version_number: int | Unset = UNSET,
    bundle_name: str | Unset = UNSET,
    bundle_version: None | str | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
) -> DAGVersionCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dag Versions

     Get all DAG Versions.

    This endpoint allows specifying `~` as the dag_id to retrieve DAG Versions for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        version_number (int | Unset):
        bundle_name (str | Unset):
        bundle_version (None | str | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, version_number,
            bundle_name, bundle_version`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGVersionCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        limit=limit,
        offset=offset,
        version_number=version_number,
        bundle_name=bundle_name,
        bundle_version=bundle_version,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    version_number: int | Unset = UNSET,
    bundle_name: str | Unset = UNSET,
    bundle_version: None | str | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
) -> Response[DAGVersionCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dag Versions

     Get all DAG Versions.

    This endpoint allows specifying `~` as the dag_id to retrieve DAG Versions for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        version_number (int | Unset):
        bundle_name (str | Unset):
        bundle_version (None | str | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, version_number,
            bundle_name, bundle_version`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGVersionCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        limit=limit,
        offset=offset,
        version_number=version_number,
        bundle_name=bundle_name,
        bundle_version=bundle_version,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    version_number: int | Unset = UNSET,
    bundle_name: str | Unset = UNSET,
    bundle_version: None | str | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
) -> DAGVersionCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dag Versions

     Get all DAG Versions.

    This endpoint allows specifying `~` as the dag_id to retrieve DAG Versions for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        version_number (int | Unset):
        bundle_name (str | Unset):
        bundle_version (None | str | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, version_number,
            bundle_name, bundle_version`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGVersionCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            limit=limit,
            offset=offset,
            version_number=version_number,
            bundle_name=bundle_name,
            bundle_version=bundle_version,
            order_by=order_by,
        )
    ).parsed

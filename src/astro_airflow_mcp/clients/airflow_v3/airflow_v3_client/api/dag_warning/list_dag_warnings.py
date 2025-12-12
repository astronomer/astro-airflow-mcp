from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_warning_collection_response import DAGWarningCollectionResponse
from ...models.dag_warning_type import DagWarningType
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    dag_id: None | str | Unset = UNSET,
    warning_type: DagWarningType | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_dag_id: None | str | Unset
    if isinstance(dag_id, Unset):
        json_dag_id = UNSET
    else:
        json_dag_id = dag_id
    params["dag_id"] = json_dag_id

    json_warning_type: None | str | Unset
    if isinstance(warning_type, Unset):
        json_warning_type = UNSET
    elif isinstance(warning_type, DagWarningType):
        json_warning_type = warning_type.value
    else:
        json_warning_type = warning_type
    params["warning_type"] = json_warning_type

    params["limit"] = limit

    params["offset"] = offset

    json_order_by: list[str] | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["order_by"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dagWarnings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGWarningCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DAGWarningCollectionResponse.from_dict(response.json())

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
) -> Response[DAGWarningCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    dag_id: None | str | Unset = UNSET,
    warning_type: DagWarningType | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
) -> Response[DAGWarningCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """List Dag Warnings

     Get a list of DAG warnings.

    Args:
        dag_id (None | str | Unset):
        warning_type (DagWarningType | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `dag_id, warning_type,
            message, timestamp`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGWarningCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        warning_type=warning_type,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    dag_id: None | str | Unset = UNSET,
    warning_type: DagWarningType | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
) -> DAGWarningCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """List Dag Warnings

     Get a list of DAG warnings.

    Args:
        dag_id (None | str | Unset):
        warning_type (DagWarningType | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `dag_id, warning_type,
            message, timestamp`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGWarningCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        dag_id=dag_id,
        warning_type=warning_type,
        limit=limit,
        offset=offset,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    dag_id: None | str | Unset = UNSET,
    warning_type: DagWarningType | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
) -> Response[DAGWarningCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """List Dag Warnings

     Get a list of DAG warnings.

    Args:
        dag_id (None | str | Unset):
        warning_type (DagWarningType | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `dag_id, warning_type,
            message, timestamp`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGWarningCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        warning_type=warning_type,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    dag_id: None | str | Unset = UNSET,
    warning_type: DagWarningType | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
) -> DAGWarningCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """List Dag Warnings

     Get a list of DAG warnings.

    Args:
        dag_id (None | str | Unset):
        warning_type (DagWarningType | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `dag_id, warning_type,
            message, timestamp`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGWarningCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            dag_id=dag_id,
            warning_type=warning_type,
            limit=limit,
            offset=offset,
            order_by=order_by,
        )
    ).parsed

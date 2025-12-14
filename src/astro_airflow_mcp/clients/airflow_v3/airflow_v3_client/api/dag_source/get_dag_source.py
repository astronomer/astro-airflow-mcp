from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_source_response import DAGSourceResponse
from ...models.get_dag_source_accept import GetDagSourceAccept
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    *,
    version_number: int | None | Unset = UNSET,
    accept: GetDagSourceAccept | Unset = GetDagSourceAccept.VALUE_2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["accept"] = str(accept)

    params: dict[str, Any] = {}

    json_version_number: int | None | Unset
    if isinstance(version_number, Unset):
        json_version_number = UNSET
    else:
        json_version_number = version_number
    params["version_number"] = json_version_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dagSources/{dag_id}".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGSourceResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DAGSourceResponse.from_dict(response.json())

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

    if response.status_code == 406:
        response_406 = HTTPExceptionResponse.from_dict(response.json())

        return response_406

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DAGSourceResponse | HTTPExceptionResponse | HTTPValidationError]:
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
    version_number: int | None | Unset = UNSET,
    accept: GetDagSourceAccept | Unset = GetDagSourceAccept.VALUE_2,
) -> Response[DAGSourceResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dag Source

     Get source code using file token.

    Args:
        dag_id (str):
        version_number (int | None | Unset):
        accept (GetDagSourceAccept | Unset):  Default: GetDagSourceAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGSourceResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        version_number=version_number,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    version_number: int | None | Unset = UNSET,
    accept: GetDagSourceAccept | Unset = GetDagSourceAccept.VALUE_2,
) -> DAGSourceResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dag Source

     Get source code using file token.

    Args:
        dag_id (str):
        version_number (int | None | Unset):
        accept (GetDagSourceAccept | Unset):  Default: GetDagSourceAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGSourceResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        version_number=version_number,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    version_number: int | None | Unset = UNSET,
    accept: GetDagSourceAccept | Unset = GetDagSourceAccept.VALUE_2,
) -> Response[DAGSourceResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dag Source

     Get source code using file token.

    Args:
        dag_id (str):
        version_number (int | None | Unset):
        accept (GetDagSourceAccept | Unset):  Default: GetDagSourceAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGSourceResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        version_number=version_number,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    version_number: int | None | Unset = UNSET,
    accept: GetDagSourceAccept | Unset = GetDagSourceAccept.VALUE_2,
) -> DAGSourceResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dag Source

     Get source code using file token.

    Args:
        dag_id (str):
        version_number (int | None | Unset):
        accept (GetDagSourceAccept | Unset):  Default: GetDagSourceAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGSourceResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            version_number=version_number,
            accept=accept,
        )
    ).parsed

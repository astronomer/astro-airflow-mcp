from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionBody")


@_attrs_define
class ConnectionBody:
    """Connection Serializer for requests body.

    Attributes:
        connection_id (str):
        conn_type (str):
        description (None | str | Unset):
        host (None | str | Unset):
        login (None | str | Unset):
        schema (None | str | Unset):
        port (int | None | Unset):
        password (None | str | Unset):
        extra (None | str | Unset):
    """

    connection_id: str
    conn_type: str
    description: None | str | Unset = UNSET
    host: None | str | Unset = UNSET
    login: None | str | Unset = UNSET
    schema: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    password: None | str | Unset = UNSET
    extra: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        conn_type = self.conn_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        login: None | str | Unset
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        schema: None | str | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        else:
            schema = self.schema

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        extra: None | str | Unset
        if isinstance(self.extra, Unset):
            extra = UNSET
        else:
            extra = self.extra

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "connection_id": connection_id,
                "conn_type": conn_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if host is not UNSET:
            field_dict["host"] = host
        if login is not UNSET:
            field_dict["login"] = login
        if schema is not UNSET:
            field_dict["schema"] = schema
        if port is not UNSET:
            field_dict["port"] = port
        if password is not UNSET:
            field_dict["password"] = password
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connection_id")

        conn_type = d.pop("conn_type")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_login(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        login = _parse_login(d.pop("login", UNSET))

        def _parse_schema(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_extra(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extra = _parse_extra(d.pop("extra", UNSET))

        connection_body = cls(
            connection_id=connection_id,
            conn_type=conn_type,
            description=description,
            host=host,
            login=login,
            schema=schema,
            port=port,
            password=password,
            extra=extra,
        )

        return connection_body

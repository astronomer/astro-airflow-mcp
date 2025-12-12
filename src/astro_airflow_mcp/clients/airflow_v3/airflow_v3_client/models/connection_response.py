from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConnectionResponse")


@_attrs_define
class ConnectionResponse:
    """Connection serializer for responses.

    Attributes:
        connection_id (str):
        conn_type (str):
        description (None | str):
        host (None | str):
        login (None | str):
        schema (None | str):
        port (int | None):
        password (None | str):
        extra (None | str):
    """

    connection_id: str
    conn_type: str
    description: None | str
    host: None | str
    login: None | str
    schema: None | str
    port: int | None
    password: None | str
    extra: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        conn_type = self.conn_type

        description: None | str
        description = self.description

        host: None | str
        host = self.host

        login: None | str
        login = self.login

        schema: None | str
        schema = self.schema

        port: int | None
        port = self.port

        password: None | str
        password = self.password

        extra: None | str
        extra = self.extra

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_id": connection_id,
                "conn_type": conn_type,
                "description": description,
                "host": host,
                "login": login,
                "schema": schema,
                "port": port,
                "password": password,
                "extra": extra,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connection_id")

        conn_type = d.pop("conn_type")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_host(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        host = _parse_host(d.pop("host"))

        def _parse_login(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        login = _parse_login(d.pop("login"))

        def _parse_schema(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        schema = _parse_schema(d.pop("schema"))

        def _parse_port(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        port = _parse_port(d.pop("port"))

        def _parse_password(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        password = _parse_password(d.pop("password"))

        def _parse_extra(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        extra = _parse_extra(d.pop("extra"))

        connection_response = cls(
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

        connection_response.additional_properties = d
        return connection_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

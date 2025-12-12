from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionCollectionItem")


@_attrs_define
class ConnectionCollectionItem:
    """Connection collection item.
    The password and extra fields are only available when retrieving a single object due to the sensitivity of this
    data.

        Attributes:
            connection_id (str | Unset): The connection ID.
            conn_type (str | Unset): The connection type.
            description (None | str | Unset): The description of the connection.
            host (None | str | Unset): Host of the connection.
            login (None | str | Unset): Login of the connection.
            schema (None | str | Unset): Schema of the connection.
            port (int | None | Unset): Port of the connection.
    """

    connection_id: str | Unset = UNSET
    conn_type: str | Unset = UNSET
    description: None | str | Unset = UNSET
    host: None | str | Unset = UNSET
    login: None | str | Unset = UNSET
    schema: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if conn_type is not UNSET:
            field_dict["conn_type"] = conn_type
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connection_id", UNSET)

        conn_type = d.pop("conn_type", UNSET)

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

        connection_collection_item = cls(
            connection_id=connection_id,
            conn_type=conn_type,
            description=description,
            host=host,
            login=login,
            schema=schema,
            port=port,
        )

        connection_collection_item.additional_properties = d
        return connection_collection_item

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

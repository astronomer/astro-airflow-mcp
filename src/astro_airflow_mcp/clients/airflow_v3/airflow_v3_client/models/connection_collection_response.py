from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.connection_response import ConnectionResponse


T = TypeVar("T", bound="ConnectionCollectionResponse")


@_attrs_define
class ConnectionCollectionResponse:
    """Connection Collection serializer for responses.

    Attributes:
        connections (list[ConnectionResponse]):
        total_entries (int):
    """

    connections: list[ConnectionResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connections = []
        for connections_item_data in self.connections:
            connections_item = connections_item_data.to_dict()
            connections.append(connections_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connections": connections,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_response import ConnectionResponse

        d = dict(src_dict)
        connections = []
        _connections = d.pop("connections")
        for connections_item_data in _connections:
            connections_item = ConnectionResponse.from_dict(connections_item_data)

            connections.append(connections_item)

        total_entries = d.pop("total_entries")

        connection_collection_response = cls(
            connections=connections,
            total_entries=total_entries,
        )

        connection_collection_response.additional_properties = d
        return connection_collection_response

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

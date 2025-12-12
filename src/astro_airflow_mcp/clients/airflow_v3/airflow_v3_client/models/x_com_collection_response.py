from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.x_com_response import XComResponse


T = TypeVar("T", bound="XComCollectionResponse")


@_attrs_define
class XComCollectionResponse:
    """XCom Collection serializer for responses.

    Attributes:
        xcom_entries (list[XComResponse]):
        total_entries (int):
    """

    xcom_entries: list[XComResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        xcom_entries = []
        for xcom_entries_item_data in self.xcom_entries:
            xcom_entries_item = xcom_entries_item_data.to_dict()
            xcom_entries.append(xcom_entries_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "xcom_entries": xcom_entries,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.x_com_response import XComResponse

        d = dict(src_dict)
        xcom_entries = []
        _xcom_entries = d.pop("xcom_entries")
        for xcom_entries_item_data in _xcom_entries:
            xcom_entries_item = XComResponse.from_dict(xcom_entries_item_data)

            xcom_entries.append(xcom_entries_item)

        total_entries = d.pop("total_entries")

        x_com_collection_response = cls(
            xcom_entries=xcom_entries,
            total_entries=total_entries,
        )

        x_com_collection_response.additional_properties = d
        return x_com_collection_response

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

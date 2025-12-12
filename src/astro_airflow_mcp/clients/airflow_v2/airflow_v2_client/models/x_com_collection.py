from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.x_com_collection_item import XComCollectionItem


T = TypeVar("T", bound="XComCollection")


@_attrs_define
class XComCollection:
    """Collection of XCom entries.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.

        Attributes:
            total_entries (int | Unset): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            xcom_entries (list[XComCollectionItem] | Unset):
    """

    total_entries: int | Unset = UNSET
    xcom_entries: list[XComCollectionItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_entries = self.total_entries

        xcom_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.xcom_entries, Unset):
            xcom_entries = []
            for xcom_entries_item_data in self.xcom_entries:
                xcom_entries_item = xcom_entries_item_data.to_dict()
                xcom_entries.append(xcom_entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if xcom_entries is not UNSET:
            field_dict["xcom_entries"] = xcom_entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.x_com_collection_item import XComCollectionItem

        d = dict(src_dict)
        total_entries = d.pop("total_entries", UNSET)

        _xcom_entries = d.pop("xcom_entries", UNSET)
        xcom_entries: list[XComCollectionItem] | Unset = UNSET
        if _xcom_entries is not UNSET:
            xcom_entries = []
            for xcom_entries_item_data in _xcom_entries:
                xcom_entries_item = XComCollectionItem.from_dict(xcom_entries_item_data)

                xcom_entries.append(xcom_entries_item)

        x_com_collection = cls(
            total_entries=total_entries,
            xcom_entries=xcom_entries,
        )

        x_com_collection.additional_properties = d
        return x_com_collection

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

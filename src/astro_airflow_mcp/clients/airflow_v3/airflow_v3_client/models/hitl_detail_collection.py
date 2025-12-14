from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hitl_detail import HITLDetail


T = TypeVar("T", bound="HITLDetailCollection")


@_attrs_define
class HITLDetailCollection:
    """Schema for a collection of Human-in-the-loop details.

    Attributes:
        hitl_details (list[HITLDetail]):
        total_entries (int):
    """

    hitl_details: list[HITLDetail]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hitl_details = []
        for hitl_details_item_data in self.hitl_details:
            hitl_details_item = hitl_details_item_data.to_dict()
            hitl_details.append(hitl_details_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hitl_details": hitl_details,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hitl_detail import HITLDetail

        d = dict(src_dict)
        hitl_details = []
        _hitl_details = d.pop("hitl_details")
        for hitl_details_item_data in _hitl_details:
            hitl_details_item = HITLDetail.from_dict(hitl_details_item_data)

            hitl_details.append(hitl_details_item)

        total_entries = d.pop("total_entries")

        hitl_detail_collection = cls(
            hitl_details=hitl_details,
            total_entries=total_entries,
        )

        hitl_detail_collection.additional_properties = d
        return hitl_detail_collection

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

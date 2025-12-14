from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.extra_links import ExtraLinks


T = TypeVar("T", bound="ExtraLinkCollectionResponse")


@_attrs_define
class ExtraLinkCollectionResponse:
    """Extra Links Response.

    Attributes:
        extra_links (ExtraLinks):
        total_entries (int):
    """

    extra_links: ExtraLinks
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extra_links = self.extra_links.to_dict()

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extra_links": extra_links,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extra_links import ExtraLinks

        d = dict(src_dict)
        extra_links = ExtraLinks.from_dict(d.pop("extra_links"))

        total_entries = d.pop("total_entries")

        extra_link_collection_response = cls(
            extra_links=extra_links,
            total_entries=total_entries,
        )

        extra_link_collection_response.additional_properties = d
        return extra_link_collection_response

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

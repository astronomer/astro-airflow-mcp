from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extra_link import ExtraLink


T = TypeVar("T", bound="ExtraLinkCollection")


@_attrs_define
class ExtraLinkCollection:
    """The collection of extra links.

    Attributes:
        extra_links (list[ExtraLink] | Unset):
    """

    extra_links: list[ExtraLink] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extra_links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extra_links, Unset):
            extra_links = []
            for extra_links_item_data in self.extra_links:
                extra_links_item = extra_links_item_data.to_dict()
                extra_links.append(extra_links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extra_links is not UNSET:
            field_dict["extra_links"] = extra_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extra_link import ExtraLink

        d = dict(src_dict)
        _extra_links = d.pop("extra_links", UNSET)
        extra_links: list[ExtraLink] | Unset = UNSET
        if _extra_links is not UNSET:
            extra_links = []
            for extra_links_item_data in _extra_links:
                extra_links_item = ExtraLink.from_dict(extra_links_item_data)

                extra_links.append(extra_links_item)

        extra_link_collection = cls(
            extra_links=extra_links,
        )

        extra_link_collection.additional_properties = d
        return extra_link_collection

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

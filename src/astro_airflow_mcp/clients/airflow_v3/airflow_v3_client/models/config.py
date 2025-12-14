from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.config_section import ConfigSection


T = TypeVar("T", bound="Config")


@_attrs_define
class Config:
    """List of config sections with their options.

    Attributes:
        sections (list[ConfigSection]):
    """

    sections: list[ConfigSection]

    def to_dict(self) -> dict[str, Any]:
        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()
            sections.append(sections_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sections": sections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_section import ConfigSection

        d = dict(src_dict)
        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = ConfigSection.from_dict(sections_item_data)

            sections.append(sections_item)

        config = cls(
            sections=sections,
        )

        return config

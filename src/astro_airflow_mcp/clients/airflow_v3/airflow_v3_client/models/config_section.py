from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.config_option import ConfigOption


T = TypeVar("T", bound="ConfigSection")


@_attrs_define
class ConfigSection:
    """Config Section Schema.

    Attributes:
        name (str):
        options (list[ConfigOption]):
    """

    name: str
    options: list[ConfigOption]

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_option import ConfigOption

        d = dict(src_dict)
        name = d.pop("name")

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = ConfigOption.from_dict(options_item_data)

            options.append(options_item)

        config_section = cls(
            name=name,
            options=options,
        )

        return config_section

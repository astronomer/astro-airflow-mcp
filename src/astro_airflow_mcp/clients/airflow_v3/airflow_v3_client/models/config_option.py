from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ConfigOption")


@_attrs_define
class ConfigOption:
    """Config option.

    Attributes:
        key (str):
        value (list[str] | str):
    """

    key: str
    value: list[str] | str

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value: list[str] | str
        if isinstance(self.value, list):
            value = []
            for value_type_1_item_data in self.value:
                value_type_1_item: str
                value_type_1_item = value_type_1_item_data
                value.append(value_type_1_item)

        else:
            value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_value(data: object) -> list[str] | str:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_1 = []
                _value_type_1 = data
                for value_type_1_item_data in _value_type_1:

                    def _parse_value_type_1_item(data: object) -> str:
                        return cast(str, data)

                    value_type_1_item = _parse_value_type_1_item(value_type_1_item_data)

                    value_type_1.append(value_type_1_item)

                return value_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str, data)

        value = _parse_value(d.pop("value"))

        config_option = cls(
            key=key,
            value=value,
        )

        return config_option

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="XComUpdateBody")


@_attrs_define
class XComUpdateBody:
    """Payload serializer for updating an XCom entry.

    Attributes:
        value (Any):
        map_index (int | Unset):  Default: -1.
    """

    value: Any
    map_index: int | Unset = -1

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        map_index = self.map_index

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
            }
        )
        if map_index is not UNSET:
            field_dict["map_index"] = map_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        map_index = d.pop("map_index", UNSET)

        x_com_update_body = cls(
            value=value,
            map_index=map_index,
        )

        return x_com_update_body

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="XComCreateBody")


@_attrs_define
class XComCreateBody:
    """Payload serializer for creating an XCom entry.

    Attributes:
        key (str):
        value (Any):
        map_index (int | Unset):  Default: -1.
    """

    key: str
    value: Any
    map_index: int | Unset = -1

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        map_index = self.map_index

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )
        if map_index is not UNSET:
            field_dict["map_index"] = map_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        map_index = d.pop("map_index", UNSET)

        x_com_create_body = cls(
            key=key,
            value=value,
            map_index=map_index,
        )

        return x_com_create_body

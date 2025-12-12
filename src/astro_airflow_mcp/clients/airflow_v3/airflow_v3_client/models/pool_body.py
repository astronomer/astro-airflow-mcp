from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoolBody")


@_attrs_define
class PoolBody:
    """Pool serializer for post bodies.

    Attributes:
        name (str):
        slots (int):
        description (None | str | Unset):
        include_deferred (bool | Unset):  Default: False.
    """

    name: str
    slots: int
    description: None | str | Unset = UNSET
    include_deferred: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slots = self.slots

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        include_deferred = self.include_deferred

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "slots": slots,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if include_deferred is not UNSET:
            field_dict["include_deferred"] = include_deferred

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slots = d.pop("slots")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        include_deferred = d.pop("include_deferred", UNSET)

        pool_body = cls(
            name=name,
            slots=slots,
            description=description,
            include_deferred=include_deferred,
        )

        return pool_body

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoolPatchBody")


@_attrs_define
class PoolPatchBody:
    """Pool serializer for patch bodies.

    Attributes:
        pool (None | str | Unset):
        slots (int | None | Unset):
        description (None | str | Unset):
        include_deferred (bool | None | Unset):
    """

    pool: None | str | Unset = UNSET
    slots: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    include_deferred: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        pool: None | str | Unset
        if isinstance(self.pool, Unset):
            pool = UNSET
        else:
            pool = self.pool

        slots: int | None | Unset
        if isinstance(self.slots, Unset):
            slots = UNSET
        else:
            slots = self.slots

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        include_deferred: bool | None | Unset
        if isinstance(self.include_deferred, Unset):
            include_deferred = UNSET
        else:
            include_deferred = self.include_deferred

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if pool is not UNSET:
            field_dict["pool"] = pool
        if slots is not UNSET:
            field_dict["slots"] = slots
        if description is not UNSET:
            field_dict["description"] = description
        if include_deferred is not UNSET:
            field_dict["include_deferred"] = include_deferred

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_pool(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pool = _parse_pool(d.pop("pool", UNSET))

        def _parse_slots(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        slots = _parse_slots(d.pop("slots", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_include_deferred(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_deferred = _parse_include_deferred(d.pop("include_deferred", UNSET))

        pool_patch_body = cls(
            pool=pool,
            slots=slots,
            description=description,
            include_deferred=include_deferred,
        )

        return pool_patch_body

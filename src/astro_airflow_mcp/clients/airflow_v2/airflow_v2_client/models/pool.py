from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pool")


@_attrs_define
class Pool:
    """The pool

    Attributes:
        name (str | Unset): The name of pool.
        slots (int | Unset): The maximum number of slots that can be assigned to tasks. One job may occupy one or more
            slots.
        occupied_slots (int | Unset): The number of slots used by running/queued tasks at the moment. May include
            deferred tasks if 'include_deferred' is set to true.
        running_slots (int | Unset): The number of slots used by running tasks at the moment.
        queued_slots (int | Unset): The number of slots used by queued tasks at the moment.
        open_slots (int | Unset): The number of free slots at the moment.
        scheduled_slots (int | Unset): The number of slots used by scheduled tasks at the moment.
        deferred_slots (int | Unset): The number of slots used by deferred tasks at the moment. Relevant if
            'include_deferred' is set to true.

            *New in version 2.7.0*
        description (None | str | Unset): The description of the pool.

            *New in version 2.3.0*
        include_deferred (bool | Unset): If set to true, deferred tasks are considered when calculating open pool slots.

            *New in version 2.7.0*
    """

    name: str | Unset = UNSET
    slots: int | Unset = UNSET
    occupied_slots: int | Unset = UNSET
    running_slots: int | Unset = UNSET
    queued_slots: int | Unset = UNSET
    open_slots: int | Unset = UNSET
    scheduled_slots: int | Unset = UNSET
    deferred_slots: int | Unset = UNSET
    description: None | str | Unset = UNSET
    include_deferred: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slots = self.slots

        occupied_slots = self.occupied_slots

        running_slots = self.running_slots

        queued_slots = self.queued_slots

        open_slots = self.open_slots

        scheduled_slots = self.scheduled_slots

        deferred_slots = self.deferred_slots

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        include_deferred = self.include_deferred

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slots is not UNSET:
            field_dict["slots"] = slots
        if occupied_slots is not UNSET:
            field_dict["occupied_slots"] = occupied_slots
        if running_slots is not UNSET:
            field_dict["running_slots"] = running_slots
        if queued_slots is not UNSET:
            field_dict["queued_slots"] = queued_slots
        if open_slots is not UNSET:
            field_dict["open_slots"] = open_slots
        if scheduled_slots is not UNSET:
            field_dict["scheduled_slots"] = scheduled_slots
        if deferred_slots is not UNSET:
            field_dict["deferred_slots"] = deferred_slots
        if description is not UNSET:
            field_dict["description"] = description
        if include_deferred is not UNSET:
            field_dict["include_deferred"] = include_deferred

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        slots = d.pop("slots", UNSET)

        occupied_slots = d.pop("occupied_slots", UNSET)

        running_slots = d.pop("running_slots", UNSET)

        queued_slots = d.pop("queued_slots", UNSET)

        open_slots = d.pop("open_slots", UNSET)

        scheduled_slots = d.pop("scheduled_slots", UNSET)

        deferred_slots = d.pop("deferred_slots", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        include_deferred = d.pop("include_deferred", UNSET)

        pool = cls(
            name=name,
            slots=slots,
            occupied_slots=occupied_slots,
            running_slots=running_slots,
            queued_slots=queued_slots,
            open_slots=open_slots,
            scheduled_slots=scheduled_slots,
            deferred_slots=deferred_slots,
            description=description,
            include_deferred=include_deferred,
        )

        pool.additional_properties = d
        return pool

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

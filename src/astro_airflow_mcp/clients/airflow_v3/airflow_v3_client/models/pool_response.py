from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PoolResponse")


@_attrs_define
class PoolResponse:
    """Pool serializer for responses.

    Attributes:
        name (str):
        slots (int):
        description (None | str):
        include_deferred (bool):
        occupied_slots (int):
        running_slots (int):
        queued_slots (int):
        scheduled_slots (int):
        open_slots (int):
        deferred_slots (int):
    """

    name: str
    slots: int
    description: None | str
    include_deferred: bool
    occupied_slots: int
    running_slots: int
    queued_slots: int
    scheduled_slots: int
    open_slots: int
    deferred_slots: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slots = self.slots

        description: None | str
        description = self.description

        include_deferred = self.include_deferred

        occupied_slots = self.occupied_slots

        running_slots = self.running_slots

        queued_slots = self.queued_slots

        scheduled_slots = self.scheduled_slots

        open_slots = self.open_slots

        deferred_slots = self.deferred_slots

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slots": slots,
                "description": description,
                "include_deferred": include_deferred,
                "occupied_slots": occupied_slots,
                "running_slots": running_slots,
                "queued_slots": queued_slots,
                "scheduled_slots": scheduled_slots,
                "open_slots": open_slots,
                "deferred_slots": deferred_slots,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slots = d.pop("slots")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        include_deferred = d.pop("include_deferred")

        occupied_slots = d.pop("occupied_slots")

        running_slots = d.pop("running_slots")

        queued_slots = d.pop("queued_slots")

        scheduled_slots = d.pop("scheduled_slots")

        open_slots = d.pop("open_slots")

        deferred_slots = d.pop("deferred_slots")

        pool_response = cls(
            name=name,
            slots=slots,
            description=description,
            include_deferred=include_deferred,
            occupied_slots=occupied_slots,
            running_slots=running_slots,
            queued_slots=queued_slots,
            scheduled_slots=scheduled_slots,
            open_slots=open_slots,
            deferred_slots=deferred_slots,
        )

        pool_response.additional_properties = d
        return pool_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TimeDeltaType0")


@_attrs_define
class TimeDeltaType0:
    """Time delta

    Attributes:
        field_type_ (str):
        days (int):
        seconds (int):
        microseconds (int):
    """

    field_type_: str
    days: int
    seconds: int
    microseconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_type_ = self.field_type_

        days = self.days

        seconds = self.seconds

        microseconds = self.microseconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "__type": field_type_,
                "days": days,
                "seconds": seconds,
                "microseconds": microseconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_type_ = d.pop("__type")

        days = d.pop("days")

        seconds = d.pop("seconds")

        microseconds = d.pop("microseconds")

        time_delta_type_0 = cls(
            field_type_=field_type_,
            days=days,
            seconds=seconds,
            microseconds=microseconds,
        )

        time_delta_type_0.additional_properties = d
        return time_delta_type_0

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

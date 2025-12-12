from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RelativeDelta")


@_attrs_define
class RelativeDelta:
    """Relative delta

    Attributes:
        field_type_ (str):
        years (int):
        months (int):
        days (int):
        leapdays (int):
        hours (int):
        minutes (int):
        seconds (int):
        microseconds (int):
        year (int):
        month (int):
        day (int):
        hour (int):
        minute (int):
        second (int):
        microsecond (int):
    """

    field_type_: str
    years: int
    months: int
    days: int
    leapdays: int
    hours: int
    minutes: int
    seconds: int
    microseconds: int
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int
    microsecond: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_type_ = self.field_type_

        years = self.years

        months = self.months

        days = self.days

        leapdays = self.leapdays

        hours = self.hours

        minutes = self.minutes

        seconds = self.seconds

        microseconds = self.microseconds

        year = self.year

        month = self.month

        day = self.day

        hour = self.hour

        minute = self.minute

        second = self.second

        microsecond = self.microsecond

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "__type": field_type_,
                "years": years,
                "months": months,
                "days": days,
                "leapdays": leapdays,
                "hours": hours,
                "minutes": minutes,
                "seconds": seconds,
                "microseconds": microseconds,
                "year": year,
                "month": month,
                "day": day,
                "hour": hour,
                "minute": minute,
                "second": second,
                "microsecond": microsecond,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_type_ = d.pop("__type")

        years = d.pop("years")

        months = d.pop("months")

        days = d.pop("days")

        leapdays = d.pop("leapdays")

        hours = d.pop("hours")

        minutes = d.pop("minutes")

        seconds = d.pop("seconds")

        microseconds = d.pop("microseconds")

        year = d.pop("year")

        month = d.pop("month")

        day = d.pop("day")

        hour = d.pop("hour")

        minute = d.pop("minute")

        second = d.pop("second")

        microsecond = d.pop("microsecond")

        relative_delta = cls(
            field_type_=field_type_,
            years=years,
            months=months,
            days=days,
            leapdays=leapdays,
            hours=hours,
            minutes=minutes,
            seconds=seconds,
            microseconds=microseconds,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=microsecond,
        )

        relative_delta.additional_properties = d
        return relative_delta

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

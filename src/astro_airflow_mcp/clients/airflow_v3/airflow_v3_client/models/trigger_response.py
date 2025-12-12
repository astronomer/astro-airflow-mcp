from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="TriggerResponse")


@_attrs_define
class TriggerResponse:
    """Trigger serializer for responses.

    Attributes:
        id (int):
        classpath (str):
        kwargs (str):
        created_date (datetime.datetime):
        triggerer_id (int | None):
    """

    id: int
    classpath: str
    kwargs: str
    created_date: datetime.datetime
    triggerer_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        classpath = self.classpath

        kwargs = self.kwargs

        created_date = self.created_date.isoformat()

        triggerer_id: int | None
        triggerer_id = self.triggerer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "classpath": classpath,
                "kwargs": kwargs,
                "created_date": created_date,
                "triggerer_id": triggerer_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        classpath = d.pop("classpath")

        kwargs = d.pop("kwargs")

        created_date = isoparse(d.pop("created_date"))

        def _parse_triggerer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        triggerer_id = _parse_triggerer_id(d.pop("triggerer_id"))

        trigger_response = cls(
            id=id,
            classpath=classpath,
            kwargs=kwargs,
            created_date=created_date,
            triggerer_id=triggerer_id,
        )

        trigger_response.additional_properties = d
        return trigger_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SchedulerInfoResponse")


@_attrs_define
class SchedulerInfoResponse:
    """Scheduler info serializer for responses.

    Attributes:
        status (None | str):
        latest_scheduler_heartbeat (None | str):
    """

    status: None | str
    latest_scheduler_heartbeat: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: None | str
        status = self.status

        latest_scheduler_heartbeat: None | str
        latest_scheduler_heartbeat = self.latest_scheduler_heartbeat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "latest_scheduler_heartbeat": latest_scheduler_heartbeat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_latest_scheduler_heartbeat(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latest_scheduler_heartbeat = _parse_latest_scheduler_heartbeat(d.pop("latest_scheduler_heartbeat"))

        scheduler_info_response = cls(
            status=status,
            latest_scheduler_heartbeat=latest_scheduler_heartbeat,
        )

        scheduler_info_response.additional_properties = d
        return scheduler_info_response

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

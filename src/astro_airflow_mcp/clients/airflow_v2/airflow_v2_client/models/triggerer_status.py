from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.health_status import HealthStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggererStatus")


@_attrs_define
class TriggererStatus:
    """The status and the latest triggerer heartbeat.

    *New in version 2.6.2*

        Attributes:
            status (HealthStatus | Unset): Health status
            latest_triggerer_heartbeat (None | str | Unset): The time the triggerer last did a heartbeat.
    """

    status: HealthStatus | Unset = UNSET
    latest_triggerer_heartbeat: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        latest_triggerer_heartbeat: None | str | Unset
        if isinstance(self.latest_triggerer_heartbeat, Unset):
            latest_triggerer_heartbeat = UNSET
        else:
            latest_triggerer_heartbeat = self.latest_triggerer_heartbeat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if latest_triggerer_heartbeat is not UNSET:
            field_dict["latest_triggerer_heartbeat"] = latest_triggerer_heartbeat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: HealthStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HealthStatus(_status)

        def _parse_latest_triggerer_heartbeat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_triggerer_heartbeat = _parse_latest_triggerer_heartbeat(d.pop("latest_triggerer_heartbeat", UNSET))

        triggerer_status = cls(
            status=status,
            latest_triggerer_heartbeat=latest_triggerer_heartbeat,
        )

        triggerer_status.additional_properties = d
        return triggerer_status

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

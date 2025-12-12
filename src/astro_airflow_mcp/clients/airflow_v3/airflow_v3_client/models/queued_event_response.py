from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="QueuedEventResponse")


@_attrs_define
class QueuedEventResponse:
    """Queued Event serializer for responses..

    Attributes:
        dag_id (str):
        asset_id (int):
        created_at (datetime.datetime):
        dag_display_name (str):
    """

    dag_id: str
    asset_id: int
    created_at: datetime.datetime
    dag_display_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dag_id = self.dag_id

        asset_id = self.asset_id

        created_at = self.created_at.isoformat()

        dag_display_name = self.dag_display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dag_id": dag_id,
                "asset_id": asset_id,
                "created_at": created_at,
                "dag_display_name": dag_display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dag_id = d.pop("dag_id")

        asset_id = d.pop("asset_id")

        created_at = isoparse(d.pop("created_at"))

        dag_display_name = d.pop("dag_display_name")

        queued_event_response = cls(
            dag_id=dag_id,
            asset_id=asset_id,
            created_at=created_at,
            dag_display_name=dag_display_name,
        )

        queued_event_response.additional_properties = d
        return queued_event_response

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

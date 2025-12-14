from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SLAMissType0")


@_attrs_define
class SLAMissType0:
    """
    Attributes:
        task_id (str | Unset): The task ID.
        dag_id (str | Unset): The DAG ID.
        execution_date (str | Unset):
        email_sent (bool | Unset):
        timestamp (str | Unset):
        description (None | str | Unset):
        notification_sent (bool | Unset):
    """

    task_id: str | Unset = UNSET
    dag_id: str | Unset = UNSET
    execution_date: str | Unset = UNSET
    email_sent: bool | Unset = UNSET
    timestamp: str | Unset = UNSET
    description: None | str | Unset = UNSET
    notification_sent: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        dag_id = self.dag_id

        execution_date = self.execution_date

        email_sent = self.email_sent

        timestamp = self.timestamp

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        notification_sent = self.notification_sent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if email_sent is not UNSET:
            field_dict["email_sent"] = email_sent
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if description is not UNSET:
            field_dict["description"] = description
        if notification_sent is not UNSET:
            field_dict["notification_sent"] = notification_sent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("task_id", UNSET)

        dag_id = d.pop("dag_id", UNSET)

        execution_date = d.pop("execution_date", UNSET)

        email_sent = d.pop("email_sent", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        notification_sent = d.pop("notification_sent", UNSET)

        sla_miss_type_0 = cls(
            task_id=task_id,
            dag_id=dag_id,
            execution_date=execution_date,
            email_sent=email_sent,
            timestamp=timestamp,
            description=description,
            notification_sent=notification_sent,
        )

        sla_miss_type_0.additional_properties = d
        return sla_miss_type_0

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

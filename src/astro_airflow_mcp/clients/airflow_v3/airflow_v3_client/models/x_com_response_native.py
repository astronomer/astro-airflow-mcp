from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="XComResponseNative")


@_attrs_define
class XComResponseNative:
    """XCom response serializer with native return type.

    Attributes:
        key (str):
        timestamp (datetime.datetime):
        logical_date (datetime.datetime | None):
        map_index (int):
        task_id (str):
        dag_id (str):
        run_id (str):
        dag_display_name (str):
        task_display_name (str):
        value (Any):
    """

    key: str
    timestamp: datetime.datetime
    logical_date: datetime.datetime | None
    map_index: int
    task_id: str
    dag_id: str
    run_id: str
    dag_display_name: str
    task_display_name: str
    value: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        timestamp = self.timestamp.isoformat()

        logical_date: None | str
        if isinstance(self.logical_date, datetime.datetime):
            logical_date = self.logical_date.isoformat()
        else:
            logical_date = self.logical_date

        map_index = self.map_index

        task_id = self.task_id

        dag_id = self.dag_id

        run_id = self.run_id

        dag_display_name = self.dag_display_name

        task_display_name = self.task_display_name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "timestamp": timestamp,
                "logical_date": logical_date,
                "map_index": map_index,
                "task_id": task_id,
                "dag_id": dag_id,
                "run_id": run_id,
                "dag_display_name": dag_display_name,
                "task_display_name": task_display_name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        timestamp = isoparse(d.pop("timestamp"))

        def _parse_logical_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logical_date_type_0 = isoparse(data)

                return logical_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        logical_date = _parse_logical_date(d.pop("logical_date"))

        map_index = d.pop("map_index")

        task_id = d.pop("task_id")

        dag_id = d.pop("dag_id")

        run_id = d.pop("run_id")

        dag_display_name = d.pop("dag_display_name")

        task_display_name = d.pop("task_display_name")

        value = d.pop("value")

        x_com_response_native = cls(
            key=key,
            timestamp=timestamp,
            logical_date=logical_date,
            map_index=map_index,
            task_id=task_id,
            dag_id=dag_id,
            run_id=run_id,
            dag_display_name=dag_display_name,
            task_display_name=task_display_name,
            value=value,
        )

        x_com_response_native.additional_properties = d
        return x_com_response_native

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

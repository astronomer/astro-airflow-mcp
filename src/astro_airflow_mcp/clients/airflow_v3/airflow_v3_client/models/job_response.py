from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobResponse")


@_attrs_define
class JobResponse:
    """Job serializer for responses.

    Attributes:
        id (int):
        dag_id (None | str):
        state (None | str):
        job_type (None | str):
        start_date (datetime.datetime | None):
        end_date (datetime.datetime | None):
        latest_heartbeat (datetime.datetime | None):
        executor_class (None | str):
        hostname (None | str):
        unixname (None | str):
        dag_display_name (None | str | Unset):
    """

    id: int
    dag_id: None | str
    state: None | str
    job_type: None | str
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    latest_heartbeat: datetime.datetime | None
    executor_class: None | str
    hostname: None | str
    unixname: None | str
    dag_display_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        dag_id: None | str
        dag_id = self.dag_id

        state: None | str
        state = self.state

        job_type: None | str
        job_type = self.job_type

        start_date: None | str
        if isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str
        if isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        latest_heartbeat: None | str
        if isinstance(self.latest_heartbeat, datetime.datetime):
            latest_heartbeat = self.latest_heartbeat.isoformat()
        else:
            latest_heartbeat = self.latest_heartbeat

        executor_class: None | str
        executor_class = self.executor_class

        hostname: None | str
        hostname = self.hostname

        unixname: None | str
        unixname = self.unixname

        dag_display_name: None | str | Unset
        if isinstance(self.dag_display_name, Unset):
            dag_display_name = UNSET
        else:
            dag_display_name = self.dag_display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "dag_id": dag_id,
                "state": state,
                "job_type": job_type,
                "start_date": start_date,
                "end_date": end_date,
                "latest_heartbeat": latest_heartbeat,
                "executor_class": executor_class,
                "hostname": hostname,
                "unixname": unixname,
            }
        )
        if dag_display_name is not UNSET:
            field_dict["dag_display_name"] = dag_display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_dag_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dag_id = _parse_dag_id(d.pop("dag_id"))

        def _parse_state(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state = _parse_state(d.pop("state"))

        def _parse_job_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        job_type = _parse_job_type(d.pop("job_type"))

        def _parse_start_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        start_date = _parse_start_date(d.pop("start_date"))

        def _parse_end_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        end_date = _parse_end_date(d.pop("end_date"))

        def _parse_latest_heartbeat(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_heartbeat_type_0 = isoparse(data)

                return latest_heartbeat_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        latest_heartbeat = _parse_latest_heartbeat(d.pop("latest_heartbeat"))

        def _parse_executor_class(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        executor_class = _parse_executor_class(d.pop("executor_class"))

        def _parse_hostname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        hostname = _parse_hostname(d.pop("hostname"))

        def _parse_unixname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unixname = _parse_unixname(d.pop("unixname"))

        def _parse_dag_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dag_display_name = _parse_dag_display_name(d.pop("dag_display_name", UNSET))

        job_response = cls(
            id=id,
            dag_id=dag_id,
            state=state,
            job_type=job_type,
            start_date=start_date,
            end_date=end_date,
            latest_heartbeat=latest_heartbeat,
            executor_class=executor_class,
            hostname=hostname,
            unixname=unixname,
            dag_display_name=dag_display_name,
        )

        job_response.additional_properties = d
        return job_response

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

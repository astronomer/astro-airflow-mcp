from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobType0")


@_attrs_define
class JobType0:
    """
    Attributes:
        id (int | Unset):
        dag_id (None | str | Unset):
        state (None | str | Unset):
        job_type (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        latest_heartbeat (None | str | Unset):
        executor_class (None | str | Unset):
        hostname (None | str | Unset):
        unixname (None | str | Unset):
    """

    id: int | Unset = UNSET
    dag_id: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    job_type: None | str | Unset = UNSET
    start_date: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    latest_heartbeat: None | str | Unset = UNSET
    executor_class: None | str | Unset = UNSET
    hostname: None | str | Unset = UNSET
    unixname: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        dag_id: None | str | Unset
        if isinstance(self.dag_id, Unset):
            dag_id = UNSET
        else:
            dag_id = self.dag_id

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        job_type: None | str | Unset
        if isinstance(self.job_type, Unset):
            job_type = UNSET
        else:
            job_type = self.job_type

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        latest_heartbeat: None | str | Unset
        if isinstance(self.latest_heartbeat, Unset):
            latest_heartbeat = UNSET
        else:
            latest_heartbeat = self.latest_heartbeat

        executor_class: None | str | Unset
        if isinstance(self.executor_class, Unset):
            executor_class = UNSET
        else:
            executor_class = self.executor_class

        hostname: None | str | Unset
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        unixname: None | str | Unset
        if isinstance(self.unixname, Unset):
            unixname = UNSET
        else:
            unixname = self.unixname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if state is not UNSET:
            field_dict["state"] = state
        if job_type is not UNSET:
            field_dict["job_type"] = job_type
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if latest_heartbeat is not UNSET:
            field_dict["latest_heartbeat"] = latest_heartbeat
        if executor_class is not UNSET:
            field_dict["executor_class"] = executor_class
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if unixname is not UNSET:
            field_dict["unixname"] = unixname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_dag_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dag_id = _parse_dag_id(d.pop("dag_id", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_job_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_type = _parse_job_type(d.pop("job_type", UNSET))

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_latest_heartbeat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_heartbeat = _parse_latest_heartbeat(d.pop("latest_heartbeat", UNSET))

        def _parse_executor_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        executor_class = _parse_executor_class(d.pop("executor_class", UNSET))

        def _parse_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        def _parse_unixname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unixname = _parse_unixname(d.pop("unixname", UNSET))

        job_type_0 = cls(
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
        )

        job_type_0.additional_properties = d
        return job_type_0

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

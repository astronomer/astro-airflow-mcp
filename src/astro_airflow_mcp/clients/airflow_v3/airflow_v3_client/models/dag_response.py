from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.dag_tag_response import DagTagResponse


T = TypeVar("T", bound="DAGResponse")


@_attrs_define
class DAGResponse:
    """DAG serializer for responses.

    Attributes:
        dag_id (str):
        dag_display_name (str):
        is_paused (bool):
        is_stale (bool):
        last_parsed_time (datetime.datetime | None):
        last_parse_duration (float | None):
        last_expired (datetime.datetime | None):
        bundle_name (None | str):
        bundle_version (None | str):
        relative_fileloc (None | str):
        fileloc (str):
        description (None | str):
        timetable_summary (None | str):
        timetable_description (None | str):
        tags (list[DagTagResponse]):
        max_active_tasks (int):
        max_active_runs (int | None):
        max_consecutive_failed_dag_runs (int):
        has_task_concurrency_limits (bool):
        has_import_errors (bool):
        next_dagrun_logical_date (datetime.datetime | None):
        next_dagrun_data_interval_start (datetime.datetime | None):
        next_dagrun_data_interval_end (datetime.datetime | None):
        next_dagrun_run_after (datetime.datetime | None):
        owners (list[str]):
        file_token (str): Return file token.
    """

    dag_id: str
    dag_display_name: str
    is_paused: bool
    is_stale: bool
    last_parsed_time: datetime.datetime | None
    last_parse_duration: float | None
    last_expired: datetime.datetime | None
    bundle_name: None | str
    bundle_version: None | str
    relative_fileloc: None | str
    fileloc: str
    description: None | str
    timetable_summary: None | str
    timetable_description: None | str
    tags: list[DagTagResponse]
    max_active_tasks: int
    max_active_runs: int | None
    max_consecutive_failed_dag_runs: int
    has_task_concurrency_limits: bool
    has_import_errors: bool
    next_dagrun_logical_date: datetime.datetime | None
    next_dagrun_data_interval_start: datetime.datetime | None
    next_dagrun_data_interval_end: datetime.datetime | None
    next_dagrun_run_after: datetime.datetime | None
    owners: list[str]
    file_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dag_id = self.dag_id

        dag_display_name = self.dag_display_name

        is_paused = self.is_paused

        is_stale = self.is_stale

        last_parsed_time: None | str
        if isinstance(self.last_parsed_time, datetime.datetime):
            last_parsed_time = self.last_parsed_time.isoformat()
        else:
            last_parsed_time = self.last_parsed_time

        last_parse_duration: float | None
        last_parse_duration = self.last_parse_duration

        last_expired: None | str
        if isinstance(self.last_expired, datetime.datetime):
            last_expired = self.last_expired.isoformat()
        else:
            last_expired = self.last_expired

        bundle_name: None | str
        bundle_name = self.bundle_name

        bundle_version: None | str
        bundle_version = self.bundle_version

        relative_fileloc: None | str
        relative_fileloc = self.relative_fileloc

        fileloc = self.fileloc

        description: None | str
        description = self.description

        timetable_summary: None | str
        timetable_summary = self.timetable_summary

        timetable_description: None | str
        timetable_description = self.timetable_description

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        max_active_tasks = self.max_active_tasks

        max_active_runs: int | None
        max_active_runs = self.max_active_runs

        max_consecutive_failed_dag_runs = self.max_consecutive_failed_dag_runs

        has_task_concurrency_limits = self.has_task_concurrency_limits

        has_import_errors = self.has_import_errors

        next_dagrun_logical_date: None | str
        if isinstance(self.next_dagrun_logical_date, datetime.datetime):
            next_dagrun_logical_date = self.next_dagrun_logical_date.isoformat()
        else:
            next_dagrun_logical_date = self.next_dagrun_logical_date

        next_dagrun_data_interval_start: None | str
        if isinstance(self.next_dagrun_data_interval_start, datetime.datetime):
            next_dagrun_data_interval_start = self.next_dagrun_data_interval_start.isoformat()
        else:
            next_dagrun_data_interval_start = self.next_dagrun_data_interval_start

        next_dagrun_data_interval_end: None | str
        if isinstance(self.next_dagrun_data_interval_end, datetime.datetime):
            next_dagrun_data_interval_end = self.next_dagrun_data_interval_end.isoformat()
        else:
            next_dagrun_data_interval_end = self.next_dagrun_data_interval_end

        next_dagrun_run_after: None | str
        if isinstance(self.next_dagrun_run_after, datetime.datetime):
            next_dagrun_run_after = self.next_dagrun_run_after.isoformat()
        else:
            next_dagrun_run_after = self.next_dagrun_run_after

        owners = self.owners

        file_token = self.file_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dag_id": dag_id,
                "dag_display_name": dag_display_name,
                "is_paused": is_paused,
                "is_stale": is_stale,
                "last_parsed_time": last_parsed_time,
                "last_parse_duration": last_parse_duration,
                "last_expired": last_expired,
                "bundle_name": bundle_name,
                "bundle_version": bundle_version,
                "relative_fileloc": relative_fileloc,
                "fileloc": fileloc,
                "description": description,
                "timetable_summary": timetable_summary,
                "timetable_description": timetable_description,
                "tags": tags,
                "max_active_tasks": max_active_tasks,
                "max_active_runs": max_active_runs,
                "max_consecutive_failed_dag_runs": max_consecutive_failed_dag_runs,
                "has_task_concurrency_limits": has_task_concurrency_limits,
                "has_import_errors": has_import_errors,
                "next_dagrun_logical_date": next_dagrun_logical_date,
                "next_dagrun_data_interval_start": next_dagrun_data_interval_start,
                "next_dagrun_data_interval_end": next_dagrun_data_interval_end,
                "next_dagrun_run_after": next_dagrun_run_after,
                "owners": owners,
                "file_token": file_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag_tag_response import DagTagResponse

        d = dict(src_dict)
        dag_id = d.pop("dag_id")

        dag_display_name = d.pop("dag_display_name")

        is_paused = d.pop("is_paused")

        is_stale = d.pop("is_stale")

        def _parse_last_parsed_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_parsed_time_type_0 = isoparse(data)

                return last_parsed_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_parsed_time = _parse_last_parsed_time(d.pop("last_parsed_time"))

        def _parse_last_parse_duration(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        last_parse_duration = _parse_last_parse_duration(d.pop("last_parse_duration"))

        def _parse_last_expired(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_expired_type_0 = isoparse(data)

                return last_expired_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_expired = _parse_last_expired(d.pop("last_expired"))

        def _parse_bundle_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bundle_name = _parse_bundle_name(d.pop("bundle_name"))

        def _parse_bundle_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bundle_version = _parse_bundle_version(d.pop("bundle_version"))

        def _parse_relative_fileloc(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        relative_fileloc = _parse_relative_fileloc(d.pop("relative_fileloc"))

        fileloc = d.pop("fileloc")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_timetable_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timetable_summary = _parse_timetable_summary(d.pop("timetable_summary"))

        def _parse_timetable_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timetable_description = _parse_timetable_description(d.pop("timetable_description"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = DagTagResponse.from_dict(tags_item_data)

            tags.append(tags_item)

        max_active_tasks = d.pop("max_active_tasks")

        def _parse_max_active_runs(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_active_runs = _parse_max_active_runs(d.pop("max_active_runs"))

        max_consecutive_failed_dag_runs = d.pop("max_consecutive_failed_dag_runs")

        has_task_concurrency_limits = d.pop("has_task_concurrency_limits")

        has_import_errors = d.pop("has_import_errors")

        def _parse_next_dagrun_logical_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_logical_date_type_0 = isoparse(data)

                return next_dagrun_logical_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_dagrun_logical_date = _parse_next_dagrun_logical_date(d.pop("next_dagrun_logical_date"))

        def _parse_next_dagrun_data_interval_start(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_data_interval_start_type_0 = isoparse(data)

                return next_dagrun_data_interval_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_dagrun_data_interval_start = _parse_next_dagrun_data_interval_start(
            d.pop("next_dagrun_data_interval_start")
        )

        def _parse_next_dagrun_data_interval_end(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_data_interval_end_type_0 = isoparse(data)

                return next_dagrun_data_interval_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_dagrun_data_interval_end = _parse_next_dagrun_data_interval_end(d.pop("next_dagrun_data_interval_end"))

        def _parse_next_dagrun_run_after(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_run_after_type_0 = isoparse(data)

                return next_dagrun_run_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_dagrun_run_after = _parse_next_dagrun_run_after(d.pop("next_dagrun_run_after"))

        owners = cast(list[str], d.pop("owners"))

        file_token = d.pop("file_token")

        dag_response = cls(
            dag_id=dag_id,
            dag_display_name=dag_display_name,
            is_paused=is_paused,
            is_stale=is_stale,
            last_parsed_time=last_parsed_time,
            last_parse_duration=last_parse_duration,
            last_expired=last_expired,
            bundle_name=bundle_name,
            bundle_version=bundle_version,
            relative_fileloc=relative_fileloc,
            fileloc=fileloc,
            description=description,
            timetable_summary=timetable_summary,
            timetable_description=timetable_description,
            tags=tags,
            max_active_tasks=max_active_tasks,
            max_active_runs=max_active_runs,
            max_consecutive_failed_dag_runs=max_consecutive_failed_dag_runs,
            has_task_concurrency_limits=has_task_concurrency_limits,
            has_import_errors=has_import_errors,
            next_dagrun_logical_date=next_dagrun_logical_date,
            next_dagrun_data_interval_start=next_dagrun_data_interval_start,
            next_dagrun_data_interval_end=next_dagrun_data_interval_end,
            next_dagrun_run_after=next_dagrun_run_after,
            owners=owners,
            file_token=file_token,
        )

        dag_response.additional_properties = d
        return dag_response

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClearTaskInstancesBody")


@_attrs_define
class ClearTaskInstancesBody:
    """Request body for Clear Task Instances endpoint.

    Attributes:
        dry_run (bool | Unset):  Default: True.
        start_date (datetime.datetime | None | Unset):
        end_date (datetime.datetime | None | Unset):
        only_failed (bool | Unset):  Default: True.
        only_running (bool | Unset):  Default: False.
        reset_dag_runs (bool | Unset):  Default: True.
        task_ids (list[list[int | str] | str] | None | Unset): A list of `task_id` or [`task_id`, `map_index`]. If only
            the `task_id` is provided for a mapped task, all of its map indices will be targeted.
        dag_run_id (None | str | Unset):
        include_upstream (bool | Unset):  Default: False.
        include_downstream (bool | Unset):  Default: False.
        include_future (bool | Unset):  Default: False.
        include_past (bool | Unset):  Default: False.
        run_on_latest_version (bool | Unset): (Experimental) Run on the latest bundle version of the dag after clearing
            the task instances. Default: False.
    """

    dry_run: bool | Unset = True
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    only_failed: bool | Unset = True
    only_running: bool | Unset = False
    reset_dag_runs: bool | Unset = True
    task_ids: list[list[int | str] | str] | None | Unset = UNSET
    dag_run_id: None | str | Unset = UNSET
    include_upstream: bool | Unset = False
    include_downstream: bool | Unset = False
    include_future: bool | Unset = False
    include_past: bool | Unset = False
    run_on_latest_version: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        only_failed = self.only_failed

        only_running = self.only_running

        reset_dag_runs = self.reset_dag_runs

        task_ids: list[list[int | str] | str] | None | Unset
        if isinstance(self.task_ids, Unset):
            task_ids = UNSET
        elif isinstance(self.task_ids, list):
            task_ids = []
            for task_ids_type_0_item_data in self.task_ids:
                task_ids_type_0_item: list[int | str] | str
                if isinstance(task_ids_type_0_item_data, list):
                    task_ids_type_0_item = []
                    for task_ids_type_0_item_type_1_item_data in task_ids_type_0_item_data:
                        task_ids_type_0_item_type_1_item: int | str
                        task_ids_type_0_item_type_1_item = task_ids_type_0_item_type_1_item_data
                        task_ids_type_0_item.append(task_ids_type_0_item_type_1_item)

                else:
                    task_ids_type_0_item = task_ids_type_0_item_data
                task_ids.append(task_ids_type_0_item)

        else:
            task_ids = self.task_ids

        dag_run_id: None | str | Unset
        if isinstance(self.dag_run_id, Unset):
            dag_run_id = UNSET
        else:
            dag_run_id = self.dag_run_id

        include_upstream = self.include_upstream

        include_downstream = self.include_downstream

        include_future = self.include_future

        include_past = self.include_past

        run_on_latest_version = self.run_on_latest_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if only_failed is not UNSET:
            field_dict["only_failed"] = only_failed
        if only_running is not UNSET:
            field_dict["only_running"] = only_running
        if reset_dag_runs is not UNSET:
            field_dict["reset_dag_runs"] = reset_dag_runs
        if task_ids is not UNSET:
            field_dict["task_ids"] = task_ids
        if dag_run_id is not UNSET:
            field_dict["dag_run_id"] = dag_run_id
        if include_upstream is not UNSET:
            field_dict["include_upstream"] = include_upstream
        if include_downstream is not UNSET:
            field_dict["include_downstream"] = include_downstream
        if include_future is not UNSET:
            field_dict["include_future"] = include_future
        if include_past is not UNSET:
            field_dict["include_past"] = include_past
        if run_on_latest_version is not UNSET:
            field_dict["run_on_latest_version"] = run_on_latest_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dry_run = d.pop("dry_run", UNSET)

        def _parse_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        only_failed = d.pop("only_failed", UNSET)

        only_running = d.pop("only_running", UNSET)

        reset_dag_runs = d.pop("reset_dag_runs", UNSET)

        def _parse_task_ids(data: object) -> list[list[int | str] | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                task_ids_type_0 = []
                _task_ids_type_0 = data
                for task_ids_type_0_item_data in _task_ids_type_0:

                    def _parse_task_ids_type_0_item(data: object) -> list[int | str] | str:
                        try:
                            if not isinstance(data, list):
                                raise TypeError()
                            task_ids_type_0_item_type_1 = []
                            _task_ids_type_0_item_type_1 = data
                            for task_ids_type_0_item_type_1_item_data in _task_ids_type_0_item_type_1:

                                def _parse_task_ids_type_0_item_type_1_item(data: object) -> int | str:
                                    return cast(int | str, data)

                                task_ids_type_0_item_type_1_item = _parse_task_ids_type_0_item_type_1_item(
                                    task_ids_type_0_item_type_1_item_data
                                )

                                task_ids_type_0_item_type_1.append(task_ids_type_0_item_type_1_item)

                            return task_ids_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(list[int | str] | str, data)

                    task_ids_type_0_item = _parse_task_ids_type_0_item(task_ids_type_0_item_data)

                    task_ids_type_0.append(task_ids_type_0_item)

                return task_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[int | str] | str] | None | Unset, data)

        task_ids = _parse_task_ids(d.pop("task_ids", UNSET))

        def _parse_dag_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dag_run_id = _parse_dag_run_id(d.pop("dag_run_id", UNSET))

        include_upstream = d.pop("include_upstream", UNSET)

        include_downstream = d.pop("include_downstream", UNSET)

        include_future = d.pop("include_future", UNSET)

        include_past = d.pop("include_past", UNSET)

        run_on_latest_version = d.pop("run_on_latest_version", UNSET)

        clear_task_instances_body = cls(
            dry_run=dry_run,
            start_date=start_date,
            end_date=end_date,
            only_failed=only_failed,
            only_running=only_running,
            reset_dag_runs=reset_dag_runs,
            task_ids=task_ids,
            dag_run_id=dag_run_id,
            include_upstream=include_upstream,
            include_downstream=include_downstream,
            include_future=include_future,
            include_past=include_past,
            run_on_latest_version=run_on_latest_version,
        )

        return clear_task_instances_body

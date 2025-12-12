from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cron_expression_type_0 import CronExpressionType0
    from ..models.relative_delta import RelativeDelta
    from ..models.tag import Tag
    from ..models.time_delta_type_0 import TimeDeltaType0


T = TypeVar("T", bound="DAG")


@_attrs_define
class DAG:
    """DAG

    Attributes:
        dag_id (str | Unset): The ID of the DAG.
        dag_display_name (str | Unset): Human centric display text for the DAG.

            *New in version 2.9.0*
        root_dag_id (None | str | Unset): If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.
        is_paused (bool | None | Unset): Whether the DAG is paused.
        is_active (bool | None | Unset): Whether the DAG is currently seen by the scheduler(s).

            *New in version 2.1.1*

            *Changed in version 2.2.0*&#58; Field is read-only.
        is_subdag (bool | Unset): Whether the DAG is SubDAG.
        last_parsed_time (datetime.datetime | None | Unset): The last time the DAG was parsed.

            *New in version 2.3.0*
        last_pickled (datetime.datetime | None | Unset): The last time the DAG was pickled.

            *New in version 2.3.0*
        last_expired (datetime.datetime | None | Unset): Time when the DAG last received a refresh signal
            (e.g. the DAG's "refresh" button was clicked in the web UI)

            *New in version 2.3.0*
        scheduler_lock (bool | None | Unset): Whether (one of) the scheduler is scheduling this DAG at the moment

            *New in version 2.3.0*
        pickle_id (None | str | Unset): Foreign key to the latest pickle_id

            *New in version 2.3.0*
        default_view (None | str | Unset): Default view of the DAG inside the webserver

            *New in version 2.3.0*
        fileloc (str | Unset): The absolute path to the file.
        file_token (str | Unset): The key containing the encrypted path to the file. Encryption and decryption take
            place only on the server. This prevents the client from reading an non-DAG file. This also ensures API
            extensibility, because the format of encrypted data may change.
        owners (list[str] | Unset):
        description (None | str | Unset): User-provided DAG description, which can consist of several sentences or
            paragraphs that describe DAG contents.
        schedule_interval (CronExpressionType0 | None | RelativeDelta | TimeDeltaType0 | Unset): Schedule interval.
            Defines how often DAG runs, this object gets added to your latest task instance's
            execution_date to figure out the next schedule.
        timetable_description (None | str | Unset): Timetable/Schedule Interval description.

            *New in version 2.3.0*
        tags (list[Tag] | None | Unset): List of tags.
        max_active_tasks (int | None | Unset): Maximum number of active tasks that can be run on the DAG

            *New in version 2.3.0*
        max_active_runs (int | None | Unset): Maximum number of active DAG runs for the DAG

            *New in version 2.3.0*
        has_task_concurrency_limits (bool | None | Unset): Whether the DAG has task concurrency limits

            *New in version 2.3.0*
        has_import_errors (bool | None | Unset): Whether the DAG has import errors

            *New in version 2.3.0*
        next_dagrun (datetime.datetime | None | Unset): The logical date of the next dag run.

            *New in version 2.3.0*
        next_dagrun_data_interval_start (datetime.datetime | None | Unset): The start of the interval of the next dag
            run.

            *New in version 2.3.0*
        next_dagrun_data_interval_end (datetime.datetime | None | Unset): The end of the interval of the next dag run.

            *New in version 2.3.0*
        next_dagrun_create_after (datetime.datetime | None | Unset): Earliest time at which this ``next_dagrun`` can be
            created.

            *New in version 2.3.0*
    """

    dag_id: str | Unset = UNSET
    dag_display_name: str | Unset = UNSET
    root_dag_id: None | str | Unset = UNSET
    is_paused: bool | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    is_subdag: bool | Unset = UNSET
    last_parsed_time: datetime.datetime | None | Unset = UNSET
    last_pickled: datetime.datetime | None | Unset = UNSET
    last_expired: datetime.datetime | None | Unset = UNSET
    scheduler_lock: bool | None | Unset = UNSET
    pickle_id: None | str | Unset = UNSET
    default_view: None | str | Unset = UNSET
    fileloc: str | Unset = UNSET
    file_token: str | Unset = UNSET
    owners: list[str] | Unset = UNSET
    description: None | str | Unset = UNSET
    schedule_interval: CronExpressionType0 | None | RelativeDelta | TimeDeltaType0 | Unset = UNSET
    timetable_description: None | str | Unset = UNSET
    tags: list[Tag] | None | Unset = UNSET
    max_active_tasks: int | None | Unset = UNSET
    max_active_runs: int | None | Unset = UNSET
    has_task_concurrency_limits: bool | None | Unset = UNSET
    has_import_errors: bool | None | Unset = UNSET
    next_dagrun: datetime.datetime | None | Unset = UNSET
    next_dagrun_data_interval_start: datetime.datetime | None | Unset = UNSET
    next_dagrun_data_interval_end: datetime.datetime | None | Unset = UNSET
    next_dagrun_create_after: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cron_expression_type_0 import CronExpressionType0
        from ..models.relative_delta import RelativeDelta
        from ..models.time_delta_type_0 import TimeDeltaType0

        dag_id = self.dag_id

        dag_display_name = self.dag_display_name

        root_dag_id: None | str | Unset
        if isinstance(self.root_dag_id, Unset):
            root_dag_id = UNSET
        else:
            root_dag_id = self.root_dag_id

        is_paused: bool | None | Unset
        if isinstance(self.is_paused, Unset):
            is_paused = UNSET
        else:
            is_paused = self.is_paused

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        is_subdag = self.is_subdag

        last_parsed_time: None | str | Unset
        if isinstance(self.last_parsed_time, Unset):
            last_parsed_time = UNSET
        elif isinstance(self.last_parsed_time, datetime.datetime):
            last_parsed_time = self.last_parsed_time.isoformat()
        else:
            last_parsed_time = self.last_parsed_time

        last_pickled: None | str | Unset
        if isinstance(self.last_pickled, Unset):
            last_pickled = UNSET
        elif isinstance(self.last_pickled, datetime.datetime):
            last_pickled = self.last_pickled.isoformat()
        else:
            last_pickled = self.last_pickled

        last_expired: None | str | Unset
        if isinstance(self.last_expired, Unset):
            last_expired = UNSET
        elif isinstance(self.last_expired, datetime.datetime):
            last_expired = self.last_expired.isoformat()
        else:
            last_expired = self.last_expired

        scheduler_lock: bool | None | Unset
        if isinstance(self.scheduler_lock, Unset):
            scheduler_lock = UNSET
        else:
            scheduler_lock = self.scheduler_lock

        pickle_id: None | str | Unset
        if isinstance(self.pickle_id, Unset):
            pickle_id = UNSET
        else:
            pickle_id = self.pickle_id

        default_view: None | str | Unset
        if isinstance(self.default_view, Unset):
            default_view = UNSET
        else:
            default_view = self.default_view

        fileloc = self.fileloc

        file_token = self.file_token

        owners: list[str] | Unset = UNSET
        if not isinstance(self.owners, Unset):
            owners = self.owners

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        schedule_interval: dict[str, Any] | None | Unset
        if isinstance(self.schedule_interval, Unset):
            schedule_interval = UNSET
        elif isinstance(self.schedule_interval, TimeDeltaType0):
            schedule_interval = self.schedule_interval.to_dict()
        elif isinstance(self.schedule_interval, RelativeDelta):
            schedule_interval = self.schedule_interval.to_dict()
        elif isinstance(self.schedule_interval, CronExpressionType0):
            schedule_interval = self.schedule_interval.to_dict()
        else:
            schedule_interval = self.schedule_interval

        timetable_description: None | str | Unset
        if isinstance(self.timetable_description, Unset):
            timetable_description = UNSET
        else:
            timetable_description = self.timetable_description

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        max_active_tasks: int | None | Unset
        if isinstance(self.max_active_tasks, Unset):
            max_active_tasks = UNSET
        else:
            max_active_tasks = self.max_active_tasks

        max_active_runs: int | None | Unset
        if isinstance(self.max_active_runs, Unset):
            max_active_runs = UNSET
        else:
            max_active_runs = self.max_active_runs

        has_task_concurrency_limits: bool | None | Unset
        if isinstance(self.has_task_concurrency_limits, Unset):
            has_task_concurrency_limits = UNSET
        else:
            has_task_concurrency_limits = self.has_task_concurrency_limits

        has_import_errors: bool | None | Unset
        if isinstance(self.has_import_errors, Unset):
            has_import_errors = UNSET
        else:
            has_import_errors = self.has_import_errors

        next_dagrun: None | str | Unset
        if isinstance(self.next_dagrun, Unset):
            next_dagrun = UNSET
        elif isinstance(self.next_dagrun, datetime.datetime):
            next_dagrun = self.next_dagrun.isoformat()
        else:
            next_dagrun = self.next_dagrun

        next_dagrun_data_interval_start: None | str | Unset
        if isinstance(self.next_dagrun_data_interval_start, Unset):
            next_dagrun_data_interval_start = UNSET
        elif isinstance(self.next_dagrun_data_interval_start, datetime.datetime):
            next_dagrun_data_interval_start = self.next_dagrun_data_interval_start.isoformat()
        else:
            next_dagrun_data_interval_start = self.next_dagrun_data_interval_start

        next_dagrun_data_interval_end: None | str | Unset
        if isinstance(self.next_dagrun_data_interval_end, Unset):
            next_dagrun_data_interval_end = UNSET
        elif isinstance(self.next_dagrun_data_interval_end, datetime.datetime):
            next_dagrun_data_interval_end = self.next_dagrun_data_interval_end.isoformat()
        else:
            next_dagrun_data_interval_end = self.next_dagrun_data_interval_end

        next_dagrun_create_after: None | str | Unset
        if isinstance(self.next_dagrun_create_after, Unset):
            next_dagrun_create_after = UNSET
        elif isinstance(self.next_dagrun_create_after, datetime.datetime):
            next_dagrun_create_after = self.next_dagrun_create_after.isoformat()
        else:
            next_dagrun_create_after = self.next_dagrun_create_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if dag_display_name is not UNSET:
            field_dict["dag_display_name"] = dag_display_name
        if root_dag_id is not UNSET:
            field_dict["root_dag_id"] = root_dag_id
        if is_paused is not UNSET:
            field_dict["is_paused"] = is_paused
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_subdag is not UNSET:
            field_dict["is_subdag"] = is_subdag
        if last_parsed_time is not UNSET:
            field_dict["last_parsed_time"] = last_parsed_time
        if last_pickled is not UNSET:
            field_dict["last_pickled"] = last_pickled
        if last_expired is not UNSET:
            field_dict["last_expired"] = last_expired
        if scheduler_lock is not UNSET:
            field_dict["scheduler_lock"] = scheduler_lock
        if pickle_id is not UNSET:
            field_dict["pickle_id"] = pickle_id
        if default_view is not UNSET:
            field_dict["default_view"] = default_view
        if fileloc is not UNSET:
            field_dict["fileloc"] = fileloc
        if file_token is not UNSET:
            field_dict["file_token"] = file_token
        if owners is not UNSET:
            field_dict["owners"] = owners
        if description is not UNSET:
            field_dict["description"] = description
        if schedule_interval is not UNSET:
            field_dict["schedule_interval"] = schedule_interval
        if timetable_description is not UNSET:
            field_dict["timetable_description"] = timetable_description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if max_active_tasks is not UNSET:
            field_dict["max_active_tasks"] = max_active_tasks
        if max_active_runs is not UNSET:
            field_dict["max_active_runs"] = max_active_runs
        if has_task_concurrency_limits is not UNSET:
            field_dict["has_task_concurrency_limits"] = has_task_concurrency_limits
        if has_import_errors is not UNSET:
            field_dict["has_import_errors"] = has_import_errors
        if next_dagrun is not UNSET:
            field_dict["next_dagrun"] = next_dagrun
        if next_dagrun_data_interval_start is not UNSET:
            field_dict["next_dagrun_data_interval_start"] = next_dagrun_data_interval_start
        if next_dagrun_data_interval_end is not UNSET:
            field_dict["next_dagrun_data_interval_end"] = next_dagrun_data_interval_end
        if next_dagrun_create_after is not UNSET:
            field_dict["next_dagrun_create_after"] = next_dagrun_create_after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cron_expression_type_0 import CronExpressionType0
        from ..models.relative_delta import RelativeDelta
        from ..models.tag import Tag
        from ..models.time_delta_type_0 import TimeDeltaType0

        d = dict(src_dict)
        dag_id = d.pop("dag_id", UNSET)

        dag_display_name = d.pop("dag_display_name", UNSET)

        def _parse_root_dag_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_dag_id = _parse_root_dag_id(d.pop("root_dag_id", UNSET))

        def _parse_is_paused(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_paused = _parse_is_paused(d.pop("is_paused", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        is_subdag = d.pop("is_subdag", UNSET)

        def _parse_last_parsed_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_parsed_time_type_0 = isoparse(data)

                return last_parsed_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_parsed_time = _parse_last_parsed_time(d.pop("last_parsed_time", UNSET))

        def _parse_last_pickled(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_pickled_type_0 = isoparse(data)

                return last_pickled_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_pickled = _parse_last_pickled(d.pop("last_pickled", UNSET))

        def _parse_last_expired(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_expired_type_0 = isoparse(data)

                return last_expired_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_expired = _parse_last_expired(d.pop("last_expired", UNSET))

        def _parse_scheduler_lock(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        scheduler_lock = _parse_scheduler_lock(d.pop("scheduler_lock", UNSET))

        def _parse_pickle_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pickle_id = _parse_pickle_id(d.pop("pickle_id", UNSET))

        def _parse_default_view(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_view = _parse_default_view(d.pop("default_view", UNSET))

        fileloc = d.pop("fileloc", UNSET)

        file_token = d.pop("file_token", UNSET)

        owners = cast(list[str], d.pop("owners", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_schedule_interval(
            data: object,
        ) -> CronExpressionType0 | None | RelativeDelta | TimeDeltaType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_time_delta_type_0 = TimeDeltaType0.from_dict(data)

                return componentsschemas_time_delta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schedule_interval_type_1 = RelativeDelta.from_dict(data)

                return componentsschemas_schedule_interval_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_cron_expression_type_0 = CronExpressionType0.from_dict(data)

                return componentsschemas_cron_expression_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CronExpressionType0 | None | RelativeDelta | TimeDeltaType0 | Unset, data)

        schedule_interval = _parse_schedule_interval(d.pop("schedule_interval", UNSET))

        def _parse_timetable_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timetable_description = _parse_timetable_description(d.pop("timetable_description", UNSET))

        def _parse_tags(data: object) -> list[Tag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = Tag.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Tag] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_max_active_tasks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_active_tasks = _parse_max_active_tasks(d.pop("max_active_tasks", UNSET))

        def _parse_max_active_runs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_active_runs = _parse_max_active_runs(d.pop("max_active_runs", UNSET))

        def _parse_has_task_concurrency_limits(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_task_concurrency_limits = _parse_has_task_concurrency_limits(d.pop("has_task_concurrency_limits", UNSET))

        def _parse_has_import_errors(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_import_errors = _parse_has_import_errors(d.pop("has_import_errors", UNSET))

        def _parse_next_dagrun(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_type_0 = isoparse(data)

                return next_dagrun_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_dagrun = _parse_next_dagrun(d.pop("next_dagrun", UNSET))

        def _parse_next_dagrun_data_interval_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_data_interval_start_type_0 = isoparse(data)

                return next_dagrun_data_interval_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_dagrun_data_interval_start = _parse_next_dagrun_data_interval_start(
            d.pop("next_dagrun_data_interval_start", UNSET)
        )

        def _parse_next_dagrun_data_interval_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_data_interval_end_type_0 = isoparse(data)

                return next_dagrun_data_interval_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_dagrun_data_interval_end = _parse_next_dagrun_data_interval_end(
            d.pop("next_dagrun_data_interval_end", UNSET)
        )

        def _parse_next_dagrun_create_after(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_create_after_type_0 = isoparse(data)

                return next_dagrun_create_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_dagrun_create_after = _parse_next_dagrun_create_after(d.pop("next_dagrun_create_after", UNSET))

        dag = cls(
            dag_id=dag_id,
            dag_display_name=dag_display_name,
            root_dag_id=root_dag_id,
            is_paused=is_paused,
            is_active=is_active,
            is_subdag=is_subdag,
            last_parsed_time=last_parsed_time,
            last_pickled=last_pickled,
            last_expired=last_expired,
            scheduler_lock=scheduler_lock,
            pickle_id=pickle_id,
            default_view=default_view,
            fileloc=fileloc,
            file_token=file_token,
            owners=owners,
            description=description,
            schedule_interval=schedule_interval,
            timetable_description=timetable_description,
            tags=tags,
            max_active_tasks=max_active_tasks,
            max_active_runs=max_active_runs,
            has_task_concurrency_limits=has_task_concurrency_limits,
            has_import_errors=has_import_errors,
            next_dagrun=next_dagrun,
            next_dagrun_data_interval_start=next_dagrun_data_interval_start,
            next_dagrun_data_interval_end=next_dagrun_data_interval_end,
            next_dagrun_create_after=next_dagrun_create_after,
        )

        dag.additional_properties = d
        return dag

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_state_type_1 import TaskStateType1
from ..models.task_state_type_2_type_1 import TaskStateType2Type1
from ..models.task_state_type_3_type_1 import TaskStateType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_type_0 import JobType0
    from ..models.sla_miss_type_0 import SLAMissType0
    from ..models.task_instance_rendered_fields import TaskInstanceRenderedFields
    from ..models.trigger_type_0 import TriggerType0


T = TypeVar("T", bound="TaskInstance")


@_attrs_define
class TaskInstance:
    """
    Attributes:
        task_id (str | Unset):
        task_display_name (str | Unset): Human centric display text for the task.

            *New in version 2.9.0*
        dag_id (str | Unset):
        dag_run_id (str | Unset): The DagRun ID for this task instance

            *New in version 2.3.0*
        execution_date (str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        duration (float | None | Unset):
        state (None | TaskStateType1 | TaskStateType2Type1 | TaskStateType3Type1 | Unset): Task state.

            *Changed in version 2.0.2*&#58; 'removed' is added as a possible value.

            *Changed in version 2.2.0*&#58; 'deferred' is added as a possible value.

            *Changed in version 2.4.0*&#58; 'sensing' state has been removed.
            *Changed in version 2.4.2*&#58; 'restarting' is added as a possible value

            *Changed in version 2.7.0*&#58; Field becomes nullable and null primitive is added as a possible value.
            *Changed in version 2.7.0*&#58; 'none' state is deprecated in favor of null.
        try_number (int | Unset):
        map_index (int | Unset):
        max_tries (int | Unset):
        hostname (str | Unset):
        unixname (str | Unset):
        pool (str | Unset):
        pool_slots (int | Unset):
        queue (None | str | Unset):
        priority_weight (int | None | Unset):
        operator (None | str | Unset): *Changed in version 2.1.1*&#58; Field becomes nullable.
        queued_when (None | str | Unset): The datetime that the task enter the state QUEUE, also known as queue_at
        pid (int | None | Unset):
        executor_config (str | Unset):
        sla_miss (None | SLAMissType0 | Unset):
        rendered_map_index (None | str | Unset): Rendered name of an expanded task instance, if the task is mapped.

            *New in version 2.9.0*
        rendered_fields (TaskInstanceRenderedFields | Unset): JSON object describing rendered fields.

            *New in version 2.3.0*
        trigger (None | TriggerType0 | Unset):
        triggerer_job (JobType0 | None | Unset):
        note (None | str | Unset): Contains manually entered notes by the user about the TaskInstance.

            *New in version 2.5.0*
    """

    task_id: str | Unset = UNSET
    task_display_name: str | Unset = UNSET
    dag_id: str | Unset = UNSET
    dag_run_id: str | Unset = UNSET
    execution_date: str | Unset = UNSET
    start_date: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    duration: float | None | Unset = UNSET
    state: None | TaskStateType1 | TaskStateType2Type1 | TaskStateType3Type1 | Unset = UNSET
    try_number: int | Unset = UNSET
    map_index: int | Unset = UNSET
    max_tries: int | Unset = UNSET
    hostname: str | Unset = UNSET
    unixname: str | Unset = UNSET
    pool: str | Unset = UNSET
    pool_slots: int | Unset = UNSET
    queue: None | str | Unset = UNSET
    priority_weight: int | None | Unset = UNSET
    operator: None | str | Unset = UNSET
    queued_when: None | str | Unset = UNSET
    pid: int | None | Unset = UNSET
    executor_config: str | Unset = UNSET
    sla_miss: None | SLAMissType0 | Unset = UNSET
    rendered_map_index: None | str | Unset = UNSET
    rendered_fields: TaskInstanceRenderedFields | Unset = UNSET
    trigger: None | TriggerType0 | Unset = UNSET
    triggerer_job: JobType0 | None | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.job_type_0 import JobType0
        from ..models.sla_miss_type_0 import SLAMissType0
        from ..models.trigger_type_0 import TriggerType0

        task_id = self.task_id

        task_display_name = self.task_display_name

        dag_id = self.dag_id

        dag_run_id = self.dag_run_id

        execution_date = self.execution_date

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

        duration: float | None | Unset
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, TaskStateType1):
            state = self.state.value
        elif isinstance(self.state, TaskStateType2Type1):
            state = self.state.value
        elif isinstance(self.state, TaskStateType3Type1):
            state = self.state.value
        else:
            state = self.state

        try_number = self.try_number

        map_index = self.map_index

        max_tries = self.max_tries

        hostname = self.hostname

        unixname = self.unixname

        pool = self.pool

        pool_slots = self.pool_slots

        queue: None | str | Unset
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        priority_weight: int | None | Unset
        if isinstance(self.priority_weight, Unset):
            priority_weight = UNSET
        else:
            priority_weight = self.priority_weight

        operator: None | str | Unset
        if isinstance(self.operator, Unset):
            operator = UNSET
        else:
            operator = self.operator

        queued_when: None | str | Unset
        if isinstance(self.queued_when, Unset):
            queued_when = UNSET
        else:
            queued_when = self.queued_when

        pid: int | None | Unset
        if isinstance(self.pid, Unset):
            pid = UNSET
        else:
            pid = self.pid

        executor_config = self.executor_config

        sla_miss: dict[str, Any] | None | Unset
        if isinstance(self.sla_miss, Unset):
            sla_miss = UNSET
        elif isinstance(self.sla_miss, SLAMissType0):
            sla_miss = self.sla_miss.to_dict()
        else:
            sla_miss = self.sla_miss

        rendered_map_index: None | str | Unset
        if isinstance(self.rendered_map_index, Unset):
            rendered_map_index = UNSET
        else:
            rendered_map_index = self.rendered_map_index

        rendered_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rendered_fields, Unset):
            rendered_fields = self.rendered_fields.to_dict()

        trigger: dict[str, Any] | None | Unset
        if isinstance(self.trigger, Unset):
            trigger = UNSET
        elif isinstance(self.trigger, TriggerType0):
            trigger = self.trigger.to_dict()
        else:
            trigger = self.trigger

        triggerer_job: dict[str, Any] | None | Unset
        if isinstance(self.triggerer_job, Unset):
            triggerer_job = UNSET
        elif isinstance(self.triggerer_job, JobType0):
            triggerer_job = self.triggerer_job.to_dict()
        else:
            triggerer_job = self.triggerer_job

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if task_display_name is not UNSET:
            field_dict["task_display_name"] = task_display_name
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if dag_run_id is not UNSET:
            field_dict["dag_run_id"] = dag_run_id
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if duration is not UNSET:
            field_dict["duration"] = duration
        if state is not UNSET:
            field_dict["state"] = state
        if try_number is not UNSET:
            field_dict["try_number"] = try_number
        if map_index is not UNSET:
            field_dict["map_index"] = map_index
        if max_tries is not UNSET:
            field_dict["max_tries"] = max_tries
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if unixname is not UNSET:
            field_dict["unixname"] = unixname
        if pool is not UNSET:
            field_dict["pool"] = pool
        if pool_slots is not UNSET:
            field_dict["pool_slots"] = pool_slots
        if queue is not UNSET:
            field_dict["queue"] = queue
        if priority_weight is not UNSET:
            field_dict["priority_weight"] = priority_weight
        if operator is not UNSET:
            field_dict["operator"] = operator
        if queued_when is not UNSET:
            field_dict["queued_when"] = queued_when
        if pid is not UNSET:
            field_dict["pid"] = pid
        if executor_config is not UNSET:
            field_dict["executor_config"] = executor_config
        if sla_miss is not UNSET:
            field_dict["sla_miss"] = sla_miss
        if rendered_map_index is not UNSET:
            field_dict["rendered_map_index"] = rendered_map_index
        if rendered_fields is not UNSET:
            field_dict["rendered_fields"] = rendered_fields
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if triggerer_job is not UNSET:
            field_dict["triggerer_job"] = triggerer_job
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_type_0 import JobType0
        from ..models.sla_miss_type_0 import SLAMissType0
        from ..models.task_instance_rendered_fields import TaskInstanceRenderedFields
        from ..models.trigger_type_0 import TriggerType0

        d = dict(src_dict)
        task_id = d.pop("task_id", UNSET)

        task_display_name = d.pop("task_display_name", UNSET)

        dag_id = d.pop("dag_id", UNSET)

        dag_run_id = d.pop("dag_run_id", UNSET)

        execution_date = d.pop("execution_date", UNSET)

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

        def _parse_duration(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration = _parse_duration(d.pop("duration", UNSET))

        def _parse_state(data: object) -> None | TaskStateType1 | TaskStateType2Type1 | TaskStateType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_task_state_type_1 = TaskStateType1(data)

                return componentsschemas_task_state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_task_state_type_2_type_1 = TaskStateType2Type1(data)

                return componentsschemas_task_state_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_task_state_type_3_type_1 = TaskStateType3Type1(data)

                return componentsschemas_task_state_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskStateType1 | TaskStateType2Type1 | TaskStateType3Type1 | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        try_number = d.pop("try_number", UNSET)

        map_index = d.pop("map_index", UNSET)

        max_tries = d.pop("max_tries", UNSET)

        hostname = d.pop("hostname", UNSET)

        unixname = d.pop("unixname", UNSET)

        pool = d.pop("pool", UNSET)

        pool_slots = d.pop("pool_slots", UNSET)

        def _parse_queue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queue = _parse_queue(d.pop("queue", UNSET))

        def _parse_priority_weight(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority_weight = _parse_priority_weight(d.pop("priority_weight", UNSET))

        def _parse_operator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operator = _parse_operator(d.pop("operator", UNSET))

        def _parse_queued_when(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queued_when = _parse_queued_when(d.pop("queued_when", UNSET))

        def _parse_pid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pid = _parse_pid(d.pop("pid", UNSET))

        executor_config = d.pop("executor_config", UNSET)

        def _parse_sla_miss(data: object) -> None | SLAMissType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sla_miss_type_0 = SLAMissType0.from_dict(data)

                return componentsschemas_sla_miss_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SLAMissType0 | Unset, data)

        sla_miss = _parse_sla_miss(d.pop("sla_miss", UNSET))

        def _parse_rendered_map_index(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rendered_map_index = _parse_rendered_map_index(d.pop("rendered_map_index", UNSET))

        _rendered_fields = d.pop("rendered_fields", UNSET)
        rendered_fields: TaskInstanceRenderedFields | Unset
        if isinstance(_rendered_fields, Unset):
            rendered_fields = UNSET
        else:
            rendered_fields = TaskInstanceRenderedFields.from_dict(_rendered_fields)

        def _parse_trigger(data: object) -> None | TriggerType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_trigger_type_0 = TriggerType0.from_dict(data)

                return componentsschemas_trigger_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TriggerType0 | Unset, data)

        trigger = _parse_trigger(d.pop("trigger", UNSET))

        def _parse_triggerer_job(data: object) -> JobType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_job_type_0 = JobType0.from_dict(data)

                return componentsschemas_job_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobType0 | None | Unset, data)

        triggerer_job = _parse_triggerer_job(d.pop("triggerer_job", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        task_instance = cls(
            task_id=task_id,
            task_display_name=task_display_name,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            execution_date=execution_date,
            start_date=start_date,
            end_date=end_date,
            duration=duration,
            state=state,
            try_number=try_number,
            map_index=map_index,
            max_tries=max_tries,
            hostname=hostname,
            unixname=unixname,
            pool=pool,
            pool_slots=pool_slots,
            queue=queue,
            priority_weight=priority_weight,
            operator=operator,
            queued_when=queued_when,
            pid=pid,
            executor_config=executor_config,
            sla_miss=sla_miss,
            rendered_map_index=rendered_map_index,
            rendered_fields=rendered_fields,
            trigger=trigger,
            triggerer_job=triggerer_job,
            note=note,
        )

        task_instance.additional_properties = d
        return task_instance

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.trigger_rule import TriggerRule
from ..models.weight_rule import WeightRule
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.class_reference import ClassReference
    from ..models.dag import DAG
    from ..models.task_extra_links_item import TaskExtraLinksItem
    from ..models.time_delta_type_0 import TimeDeltaType0


T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    """For details see:
    [airflow.models.baseoperator.BaseOperator](https://airflow.apache.org/docs/apache-
    airflow/stable/_api/airflow/models/baseoperator/index.html#airflow.models.baseoperator.BaseOperator)

        Attributes:
            class_ref (ClassReference | Unset): Class reference
            task_id (str | Unset):
            task_display_name (str | Unset):
            owner (str | Unset):
            start_date (datetime.datetime | Unset):
            end_date (datetime.datetime | None | Unset):
            trigger_rule (TriggerRule | Unset): Trigger rule.

                *Changed in version 2.2.0*&#58; 'none_failed_min_one_success' is added as a possible value. Deprecated 'dummy'
                and 'always' is added as a possible value

                *Changed in version 2.3.0*&#58; 'all_skipped' is added as a possible value.

                *Changed in version 2.5.0*&#58; 'one_done' is added as a possible value.

                *Changed in version 2.7.0*&#58; 'all_done_setup_success' is added as a possible value.
            extra_links (list[TaskExtraLinksItem] | Unset):
            depends_on_past (bool | Unset):
            is_mapped (bool | Unset):
            wait_for_downstream (bool | Unset):
            retries (float | Unset):
            queue (None | str | Unset):
            pool (str | Unset):
            pool_slots (float | Unset):
            execution_timeout (None | TimeDeltaType0 | Unset): Time delta
            retry_delay (None | TimeDeltaType0 | Unset): Time delta
            retry_exponential_backoff (bool | Unset):
            priority_weight (float | Unset):
            weight_rule (WeightRule | Unset): Weight rule.
            ui_color (str | Unset): Color in hexadecimal notation.
            ui_fgcolor (str | Unset): Color in hexadecimal notation.
            template_fields (list[str] | Unset):
            sub_dag (DAG | Unset): DAG
            downstream_task_ids (list[str] | Unset):
    """

    class_ref: ClassReference | Unset = UNSET
    task_id: str | Unset = UNSET
    task_display_name: str | Unset = UNSET
    owner: str | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    trigger_rule: TriggerRule | Unset = UNSET
    extra_links: list[TaskExtraLinksItem] | Unset = UNSET
    depends_on_past: bool | Unset = UNSET
    is_mapped: bool | Unset = UNSET
    wait_for_downstream: bool | Unset = UNSET
    retries: float | Unset = UNSET
    queue: None | str | Unset = UNSET
    pool: str | Unset = UNSET
    pool_slots: float | Unset = UNSET
    execution_timeout: None | TimeDeltaType0 | Unset = UNSET
    retry_delay: None | TimeDeltaType0 | Unset = UNSET
    retry_exponential_backoff: bool | Unset = UNSET
    priority_weight: float | Unset = UNSET
    weight_rule: WeightRule | Unset = UNSET
    ui_color: str | Unset = UNSET
    ui_fgcolor: str | Unset = UNSET
    template_fields: list[str] | Unset = UNSET
    sub_dag: DAG | Unset = UNSET
    downstream_task_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.time_delta_type_0 import TimeDeltaType0

        class_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.class_ref, Unset):
            class_ref = self.class_ref.to_dict()

        task_id = self.task_id

        task_display_name = self.task_display_name

        owner = self.owner

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        trigger_rule: str | Unset = UNSET
        if not isinstance(self.trigger_rule, Unset):
            trigger_rule = self.trigger_rule.value

        extra_links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extra_links, Unset):
            extra_links = []
            for extra_links_item_data in self.extra_links:
                extra_links_item = extra_links_item_data.to_dict()
                extra_links.append(extra_links_item)

        depends_on_past = self.depends_on_past

        is_mapped = self.is_mapped

        wait_for_downstream = self.wait_for_downstream

        retries = self.retries

        queue: None | str | Unset
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        pool = self.pool

        pool_slots = self.pool_slots

        execution_timeout: dict[str, Any] | None | Unset
        if isinstance(self.execution_timeout, Unset):
            execution_timeout = UNSET
        elif isinstance(self.execution_timeout, TimeDeltaType0):
            execution_timeout = self.execution_timeout.to_dict()
        else:
            execution_timeout = self.execution_timeout

        retry_delay: dict[str, Any] | None | Unset
        if isinstance(self.retry_delay, Unset):
            retry_delay = UNSET
        elif isinstance(self.retry_delay, TimeDeltaType0):
            retry_delay = self.retry_delay.to_dict()
        else:
            retry_delay = self.retry_delay

        retry_exponential_backoff = self.retry_exponential_backoff

        priority_weight = self.priority_weight

        weight_rule: str | Unset = UNSET
        if not isinstance(self.weight_rule, Unset):
            weight_rule = self.weight_rule.value

        ui_color = self.ui_color

        ui_fgcolor = self.ui_fgcolor

        template_fields: list[str] | Unset = UNSET
        if not isinstance(self.template_fields, Unset):
            template_fields = self.template_fields

        sub_dag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sub_dag, Unset):
            sub_dag = self.sub_dag.to_dict()

        downstream_task_ids: list[str] | Unset = UNSET
        if not isinstance(self.downstream_task_ids, Unset):
            downstream_task_ids = self.downstream_task_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_ref is not UNSET:
            field_dict["class_ref"] = class_ref
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if task_display_name is not UNSET:
            field_dict["task_display_name"] = task_display_name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if trigger_rule is not UNSET:
            field_dict["trigger_rule"] = trigger_rule
        if extra_links is not UNSET:
            field_dict["extra_links"] = extra_links
        if depends_on_past is not UNSET:
            field_dict["depends_on_past"] = depends_on_past
        if is_mapped is not UNSET:
            field_dict["is_mapped"] = is_mapped
        if wait_for_downstream is not UNSET:
            field_dict["wait_for_downstream"] = wait_for_downstream
        if retries is not UNSET:
            field_dict["retries"] = retries
        if queue is not UNSET:
            field_dict["queue"] = queue
        if pool is not UNSET:
            field_dict["pool"] = pool
        if pool_slots is not UNSET:
            field_dict["pool_slots"] = pool_slots
        if execution_timeout is not UNSET:
            field_dict["execution_timeout"] = execution_timeout
        if retry_delay is not UNSET:
            field_dict["retry_delay"] = retry_delay
        if retry_exponential_backoff is not UNSET:
            field_dict["retry_exponential_backoff"] = retry_exponential_backoff
        if priority_weight is not UNSET:
            field_dict["priority_weight"] = priority_weight
        if weight_rule is not UNSET:
            field_dict["weight_rule"] = weight_rule
        if ui_color is not UNSET:
            field_dict["ui_color"] = ui_color
        if ui_fgcolor is not UNSET:
            field_dict["ui_fgcolor"] = ui_fgcolor
        if template_fields is not UNSET:
            field_dict["template_fields"] = template_fields
        if sub_dag is not UNSET:
            field_dict["sub_dag"] = sub_dag
        if downstream_task_ids is not UNSET:
            field_dict["downstream_task_ids"] = downstream_task_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.class_reference import ClassReference
        from ..models.dag import DAG
        from ..models.task_extra_links_item import TaskExtraLinksItem
        from ..models.time_delta_type_0 import TimeDeltaType0

        d = dict(src_dict)
        _class_ref = d.pop("class_ref", UNSET)
        class_ref: ClassReference | Unset
        if isinstance(_class_ref, Unset):
            class_ref = UNSET
        else:
            class_ref = ClassReference.from_dict(_class_ref)

        task_id = d.pop("task_id", UNSET)

        task_display_name = d.pop("task_display_name", UNSET)

        owner = d.pop("owner", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

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

        _trigger_rule = d.pop("trigger_rule", UNSET)
        trigger_rule: TriggerRule | Unset
        if isinstance(_trigger_rule, Unset):
            trigger_rule = UNSET
        else:
            trigger_rule = TriggerRule(_trigger_rule)

        _extra_links = d.pop("extra_links", UNSET)
        extra_links: list[TaskExtraLinksItem] | Unset = UNSET
        if _extra_links is not UNSET:
            extra_links = []
            for extra_links_item_data in _extra_links:
                extra_links_item = TaskExtraLinksItem.from_dict(extra_links_item_data)

                extra_links.append(extra_links_item)

        depends_on_past = d.pop("depends_on_past", UNSET)

        is_mapped = d.pop("is_mapped", UNSET)

        wait_for_downstream = d.pop("wait_for_downstream", UNSET)

        retries = d.pop("retries", UNSET)

        def _parse_queue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queue = _parse_queue(d.pop("queue", UNSET))

        pool = d.pop("pool", UNSET)

        pool_slots = d.pop("pool_slots", UNSET)

        def _parse_execution_timeout(data: object) -> None | TimeDeltaType0 | Unset:
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
            return cast(None | TimeDeltaType0 | Unset, data)

        execution_timeout = _parse_execution_timeout(d.pop("execution_timeout", UNSET))

        def _parse_retry_delay(data: object) -> None | TimeDeltaType0 | Unset:
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
            return cast(None | TimeDeltaType0 | Unset, data)

        retry_delay = _parse_retry_delay(d.pop("retry_delay", UNSET))

        retry_exponential_backoff = d.pop("retry_exponential_backoff", UNSET)

        priority_weight = d.pop("priority_weight", UNSET)

        _weight_rule = d.pop("weight_rule", UNSET)
        weight_rule: WeightRule | Unset
        if isinstance(_weight_rule, Unset):
            weight_rule = UNSET
        else:
            weight_rule = WeightRule(_weight_rule)

        ui_color = d.pop("ui_color", UNSET)

        ui_fgcolor = d.pop("ui_fgcolor", UNSET)

        template_fields = cast(list[str], d.pop("template_fields", UNSET))

        _sub_dag = d.pop("sub_dag", UNSET)
        sub_dag: DAG | Unset
        if isinstance(_sub_dag, Unset):
            sub_dag = UNSET
        else:
            sub_dag = DAG.from_dict(_sub_dag)

        downstream_task_ids = cast(list[str], d.pop("downstream_task_ids", UNSET))

        task = cls(
            class_ref=class_ref,
            task_id=task_id,
            task_display_name=task_display_name,
            owner=owner,
            start_date=start_date,
            end_date=end_date,
            trigger_rule=trigger_rule,
            extra_links=extra_links,
            depends_on_past=depends_on_past,
            is_mapped=is_mapped,
            wait_for_downstream=wait_for_downstream,
            retries=retries,
            queue=queue,
            pool=pool,
            pool_slots=pool_slots,
            execution_timeout=execution_timeout,
            retry_delay=retry_delay,
            retry_exponential_backoff=retry_exponential_backoff,
            priority_weight=priority_weight,
            weight_rule=weight_rule,
            ui_color=ui_color,
            ui_fgcolor=ui_fgcolor,
            template_fields=template_fields,
            sub_dag=sub_dag,
            downstream_task_ids=downstream_task_ids,
        )

        task.additional_properties = d
        return task

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

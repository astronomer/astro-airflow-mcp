from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.task_response_class_ref_type_0 import TaskResponseClassRefType0
    from ..models.task_response_params_type_0 import TaskResponseParamsType0
    from ..models.time_delta import TimeDelta


T = TypeVar("T", bound="TaskResponse")


@_attrs_define
class TaskResponse:
    """Task serializer for responses.

    Attributes:
        task_id (None | str):
        task_display_name (None | str):
        owner (None | str):
        start_date (datetime.datetime | None):
        end_date (datetime.datetime | None):
        trigger_rule (None | str):
        depends_on_past (bool):
        wait_for_downstream (bool):
        retries (float | None):
        queue (None | str):
        pool (None | str):
        pool_slots (float | None):
        execution_timeout (None | TimeDelta):
        retry_delay (None | TimeDelta):
        retry_exponential_backoff (bool):
        priority_weight (float | None):
        weight_rule (None | str):
        ui_color (None | str):
        ui_fgcolor (None | str):
        template_fields (list[str] | None):
        downstream_task_ids (list[str] | None):
        doc_md (None | str):
        operator_name (None | str):
        params (None | TaskResponseParamsType0):
        class_ref (None | TaskResponseClassRefType0):
        is_mapped (bool | None):
        extra_links (list[str]): Extract and return extra_links.
    """

    task_id: None | str
    task_display_name: None | str
    owner: None | str
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    trigger_rule: None | str
    depends_on_past: bool
    wait_for_downstream: bool
    retries: float | None
    queue: None | str
    pool: None | str
    pool_slots: float | None
    execution_timeout: None | TimeDelta
    retry_delay: None | TimeDelta
    retry_exponential_backoff: bool
    priority_weight: float | None
    weight_rule: None | str
    ui_color: None | str
    ui_fgcolor: None | str
    template_fields: list[str] | None
    downstream_task_ids: list[str] | None
    doc_md: None | str
    operator_name: None | str
    params: None | TaskResponseParamsType0
    class_ref: None | TaskResponseClassRefType0
    is_mapped: bool | None
    extra_links: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_response_class_ref_type_0 import TaskResponseClassRefType0
        from ..models.task_response_params_type_0 import TaskResponseParamsType0
        from ..models.time_delta import TimeDelta

        task_id: None | str
        task_id = self.task_id

        task_display_name: None | str
        task_display_name = self.task_display_name

        owner: None | str
        owner = self.owner

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

        trigger_rule: None | str
        trigger_rule = self.trigger_rule

        depends_on_past = self.depends_on_past

        wait_for_downstream = self.wait_for_downstream

        retries: float | None
        retries = self.retries

        queue: None | str
        queue = self.queue

        pool: None | str
        pool = self.pool

        pool_slots: float | None
        pool_slots = self.pool_slots

        execution_timeout: dict[str, Any] | None
        if isinstance(self.execution_timeout, TimeDelta):
            execution_timeout = self.execution_timeout.to_dict()
        else:
            execution_timeout = self.execution_timeout

        retry_delay: dict[str, Any] | None
        if isinstance(self.retry_delay, TimeDelta):
            retry_delay = self.retry_delay.to_dict()
        else:
            retry_delay = self.retry_delay

        retry_exponential_backoff = self.retry_exponential_backoff

        priority_weight: float | None
        priority_weight = self.priority_weight

        weight_rule: None | str
        weight_rule = self.weight_rule

        ui_color: None | str
        ui_color = self.ui_color

        ui_fgcolor: None | str
        ui_fgcolor = self.ui_fgcolor

        template_fields: list[str] | None
        if isinstance(self.template_fields, list):
            template_fields = self.template_fields

        else:
            template_fields = self.template_fields

        downstream_task_ids: list[str] | None
        if isinstance(self.downstream_task_ids, list):
            downstream_task_ids = self.downstream_task_ids

        else:
            downstream_task_ids = self.downstream_task_ids

        doc_md: None | str
        doc_md = self.doc_md

        operator_name: None | str
        operator_name = self.operator_name

        params: dict[str, Any] | None
        if isinstance(self.params, TaskResponseParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        class_ref: dict[str, Any] | None
        if isinstance(self.class_ref, TaskResponseClassRefType0):
            class_ref = self.class_ref.to_dict()
        else:
            class_ref = self.class_ref

        is_mapped: bool | None
        is_mapped = self.is_mapped

        extra_links = self.extra_links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "task_display_name": task_display_name,
                "owner": owner,
                "start_date": start_date,
                "end_date": end_date,
                "trigger_rule": trigger_rule,
                "depends_on_past": depends_on_past,
                "wait_for_downstream": wait_for_downstream,
                "retries": retries,
                "queue": queue,
                "pool": pool,
                "pool_slots": pool_slots,
                "execution_timeout": execution_timeout,
                "retry_delay": retry_delay,
                "retry_exponential_backoff": retry_exponential_backoff,
                "priority_weight": priority_weight,
                "weight_rule": weight_rule,
                "ui_color": ui_color,
                "ui_fgcolor": ui_fgcolor,
                "template_fields": template_fields,
                "downstream_task_ids": downstream_task_ids,
                "doc_md": doc_md,
                "operator_name": operator_name,
                "params": params,
                "class_ref": class_ref,
                "is_mapped": is_mapped,
                "extra_links": extra_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_response_class_ref_type_0 import TaskResponseClassRefType0
        from ..models.task_response_params_type_0 import TaskResponseParamsType0
        from ..models.time_delta import TimeDelta

        d = dict(src_dict)

        def _parse_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        task_id = _parse_task_id(d.pop("task_id"))

        def _parse_task_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        task_display_name = _parse_task_display_name(d.pop("task_display_name"))

        def _parse_owner(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        owner = _parse_owner(d.pop("owner"))

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

        def _parse_trigger_rule(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        trigger_rule = _parse_trigger_rule(d.pop("trigger_rule"))

        depends_on_past = d.pop("depends_on_past")

        wait_for_downstream = d.pop("wait_for_downstream")

        def _parse_retries(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        retries = _parse_retries(d.pop("retries"))

        def _parse_queue(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        queue = _parse_queue(d.pop("queue"))

        def _parse_pool(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pool = _parse_pool(d.pop("pool"))

        def _parse_pool_slots(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        pool_slots = _parse_pool_slots(d.pop("pool_slots"))

        def _parse_execution_timeout(data: object) -> None | TimeDelta:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                execution_timeout_type_0 = TimeDelta.from_dict(data)

                return execution_timeout_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TimeDelta, data)

        execution_timeout = _parse_execution_timeout(d.pop("execution_timeout"))

        def _parse_retry_delay(data: object) -> None | TimeDelta:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retry_delay_type_0 = TimeDelta.from_dict(data)

                return retry_delay_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TimeDelta, data)

        retry_delay = _parse_retry_delay(d.pop("retry_delay"))

        retry_exponential_backoff = d.pop("retry_exponential_backoff")

        def _parse_priority_weight(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        priority_weight = _parse_priority_weight(d.pop("priority_weight"))

        def _parse_weight_rule(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        weight_rule = _parse_weight_rule(d.pop("weight_rule"))

        def _parse_ui_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ui_color = _parse_ui_color(d.pop("ui_color"))

        def _parse_ui_fgcolor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ui_fgcolor = _parse_ui_fgcolor(d.pop("ui_fgcolor"))

        def _parse_template_fields(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                template_fields_type_0 = cast(list[str], data)

                return template_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        template_fields = _parse_template_fields(d.pop("template_fields"))

        def _parse_downstream_task_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                downstream_task_ids_type_0 = cast(list[str], data)

                return downstream_task_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        downstream_task_ids = _parse_downstream_task_ids(d.pop("downstream_task_ids"))

        def _parse_doc_md(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        doc_md = _parse_doc_md(d.pop("doc_md"))

        def _parse_operator_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        operator_name = _parse_operator_name(d.pop("operator_name"))

        def _parse_params(data: object) -> None | TaskResponseParamsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = TaskResponseParamsType0.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResponseParamsType0, data)

        params = _parse_params(d.pop("params"))

        def _parse_class_ref(data: object) -> None | TaskResponseClassRefType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                class_ref_type_0 = TaskResponseClassRefType0.from_dict(data)

                return class_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResponseClassRefType0, data)

        class_ref = _parse_class_ref(d.pop("class_ref"))

        def _parse_is_mapped(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_mapped = _parse_is_mapped(d.pop("is_mapped"))

        extra_links = cast(list[str], d.pop("extra_links"))

        task_response = cls(
            task_id=task_id,
            task_display_name=task_display_name,
            owner=owner,
            start_date=start_date,
            end_date=end_date,
            trigger_rule=trigger_rule,
            depends_on_past=depends_on_past,
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
            downstream_task_ids=downstream_task_ids,
            doc_md=doc_md,
            operator_name=operator_name,
            params=params,
            class_ref=class_ref,
            is_mapped=is_mapped,
            extra_links=extra_links,
        )

        task_response.additional_properties = d
        return task_response

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

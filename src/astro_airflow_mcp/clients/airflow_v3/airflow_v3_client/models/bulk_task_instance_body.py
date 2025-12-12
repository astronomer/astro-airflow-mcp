from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.task_instance_state import TaskInstanceState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkTaskInstanceBody")


@_attrs_define
class BulkTaskInstanceBody:
    """Request body for bulk update, and delete task instances.

    Attributes:
        task_id (str):
        new_state (None | TaskInstanceState | Unset):
        note (None | str | Unset):
        include_upstream (bool | Unset):  Default: False.
        include_downstream (bool | Unset):  Default: False.
        include_future (bool | Unset):  Default: False.
        include_past (bool | Unset):  Default: False.
        map_index (int | None | Unset):
    """

    task_id: str
    new_state: None | TaskInstanceState | Unset = UNSET
    note: None | str | Unset = UNSET
    include_upstream: bool | Unset = False
    include_downstream: bool | Unset = False
    include_future: bool | Unset = False
    include_past: bool | Unset = False
    map_index: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        new_state: None | str | Unset
        if isinstance(self.new_state, Unset):
            new_state = UNSET
        elif isinstance(self.new_state, TaskInstanceState):
            new_state = self.new_state.value
        else:
            new_state = self.new_state

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        include_upstream = self.include_upstream

        include_downstream = self.include_downstream

        include_future = self.include_future

        include_past = self.include_past

        map_index: int | None | Unset
        if isinstance(self.map_index, Unset):
            map_index = UNSET
        else:
            map_index = self.map_index

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "task_id": task_id,
            }
        )
        if new_state is not UNSET:
            field_dict["new_state"] = new_state
        if note is not UNSET:
            field_dict["note"] = note
        if include_upstream is not UNSET:
            field_dict["include_upstream"] = include_upstream
        if include_downstream is not UNSET:
            field_dict["include_downstream"] = include_downstream
        if include_future is not UNSET:
            field_dict["include_future"] = include_future
        if include_past is not UNSET:
            field_dict["include_past"] = include_past
        if map_index is not UNSET:
            field_dict["map_index"] = map_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("task_id")

        def _parse_new_state(data: object) -> None | TaskInstanceState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                new_state_type_0 = TaskInstanceState(data)

                return new_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskInstanceState | Unset, data)

        new_state = _parse_new_state(d.pop("new_state", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        include_upstream = d.pop("include_upstream", UNSET)

        include_downstream = d.pop("include_downstream", UNSET)

        include_future = d.pop("include_future", UNSET)

        include_past = d.pop("include_past", UNSET)

        def _parse_map_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        map_index = _parse_map_index(d.pop("map_index", UNSET))

        bulk_task_instance_body = cls(
            task_id=task_id,
            new_state=new_state,
            note=note,
            include_upstream=include_upstream,
            include_downstream=include_downstream,
            include_future=include_future,
            include_past=include_past,
            map_index=map_index,
        )

        return bulk_task_instance_body

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dag_run_patch_states import DAGRunPatchStates
from ..types import UNSET, Unset

T = TypeVar("T", bound="DAGRunPatchBody")


@_attrs_define
class DAGRunPatchBody:
    """DAG Run Serializer for PATCH requests.

    Attributes:
        state (DAGRunPatchStates | None | Unset):
        note (None | str | Unset):
    """

    state: DAGRunPatchStates | None | Unset = UNSET
    note: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, DAGRunPatchStates):
            state = self.state.value
        else:
            state = self.state

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_state(data: object) -> DAGRunPatchStates | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_0 = DAGRunPatchStates(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DAGRunPatchStates | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        dag_run_patch_body = cls(
            state=state,
            note=note,
        )

        return dag_run_patch_body

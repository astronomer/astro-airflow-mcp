from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dag_run_state import DagRunState

T = TypeVar("T", bound="DagStatsStateResponse")


@_attrs_define
class DagStatsStateResponse:
    """DagStatsState serializer for responses.

    Attributes:
        state (DagRunState): All possible states that a DagRun can be in.

            These are "shared" with TaskInstanceState in some parts of the code,
            so please ensure that their values always match the ones with the
            same name in TaskInstanceState.
        count (int):
    """

    state: DagRunState
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = DagRunState(d.pop("state"))

        count = d.pop("count")

        dag_stats_state_response = cls(
            state=state,
            count=count,
        )

        dag_stats_state_response.additional_properties = d
        return dag_stats_state_response

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

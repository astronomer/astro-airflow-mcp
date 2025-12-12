from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dag_stats_state_response import DagStatsStateResponse


T = TypeVar("T", bound="DagStatsResponse")


@_attrs_define
class DagStatsResponse:
    """DAG Stats serializer for responses.

    Attributes:
        dag_id (str):
        dag_display_name (str):
        stats (list[DagStatsStateResponse]):
    """

    dag_id: str
    dag_display_name: str
    stats: list[DagStatsStateResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dag_id = self.dag_id

        dag_display_name = self.dag_display_name

        stats = []
        for stats_item_data in self.stats:
            stats_item = stats_item_data.to_dict()
            stats.append(stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dag_id": dag_id,
                "dag_display_name": dag_display_name,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag_stats_state_response import DagStatsStateResponse

        d = dict(src_dict)
        dag_id = d.pop("dag_id")

        dag_display_name = d.pop("dag_display_name")

        stats = []
        _stats = d.pop("stats")
        for stats_item_data in _stats:
            stats_item = DagStatsStateResponse.from_dict(stats_item_data)

            stats.append(stats_item)

        dag_stats_response = cls(
            dag_id=dag_id,
            dag_display_name=dag_display_name,
            stats=stats,
        )

        dag_stats_response.additional_properties = d
        return dag_stats_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_info_response import BaseInfoResponse
    from ..models.dag_processor_info_response import DagProcessorInfoResponse
    from ..models.scheduler_info_response import SchedulerInfoResponse
    from ..models.triggerer_info_response import TriggererInfoResponse


T = TypeVar("T", bound="HealthInfoResponse")


@_attrs_define
class HealthInfoResponse:
    """Health serializer for responses.

    Attributes:
        metadatabase (BaseInfoResponse): Base info serializer for responses.
        scheduler (SchedulerInfoResponse): Scheduler info serializer for responses.
        triggerer (TriggererInfoResponse): Triggerer info serializer for responses.
        dag_processor (DagProcessorInfoResponse | None | Unset):
    """

    metadatabase: BaseInfoResponse
    scheduler: SchedulerInfoResponse
    triggerer: TriggererInfoResponse
    dag_processor: DagProcessorInfoResponse | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dag_processor_info_response import DagProcessorInfoResponse

        metadatabase = self.metadatabase.to_dict()

        scheduler = self.scheduler.to_dict()

        triggerer = self.triggerer.to_dict()

        dag_processor: dict[str, Any] | None | Unset
        if isinstance(self.dag_processor, Unset):
            dag_processor = UNSET
        elif isinstance(self.dag_processor, DagProcessorInfoResponse):
            dag_processor = self.dag_processor.to_dict()
        else:
            dag_processor = self.dag_processor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadatabase": metadatabase,
                "scheduler": scheduler,
                "triggerer": triggerer,
            }
        )
        if dag_processor is not UNSET:
            field_dict["dag_processor"] = dag_processor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_info_response import BaseInfoResponse
        from ..models.dag_processor_info_response import DagProcessorInfoResponse
        from ..models.scheduler_info_response import SchedulerInfoResponse
        from ..models.triggerer_info_response import TriggererInfoResponse

        d = dict(src_dict)
        metadatabase = BaseInfoResponse.from_dict(d.pop("metadatabase"))

        scheduler = SchedulerInfoResponse.from_dict(d.pop("scheduler"))

        triggerer = TriggererInfoResponse.from_dict(d.pop("triggerer"))

        def _parse_dag_processor(data: object) -> DagProcessorInfoResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dag_processor_type_0 = DagProcessorInfoResponse.from_dict(data)

                return dag_processor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DagProcessorInfoResponse | None | Unset, data)

        dag_processor = _parse_dag_processor(d.pop("dag_processor", UNSET))

        health_info_response = cls(
            metadatabase=metadatabase,
            scheduler=scheduler,
            triggerer=triggerer,
            dag_processor=dag_processor,
        )

        health_info_response.additional_properties = d
        return health_info_response

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

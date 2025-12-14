from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_dataset_event_extra_type_0 import CreateDatasetEventExtraType0


T = TypeVar("T", bound="CreateDatasetEvent")


@_attrs_define
class CreateDatasetEvent:
    """
    Attributes:
        dataset_uri (str): The URI of the dataset
        extra (CreateDatasetEventExtraType0 | None | Unset): The dataset event extra
    """

    dataset_uri: str
    extra: CreateDatasetEventExtraType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_dataset_event_extra_type_0 import CreateDatasetEventExtraType0

        dataset_uri = self.dataset_uri

        extra: dict[str, Any] | None | Unset
        if isinstance(self.extra, Unset):
            extra = UNSET
        elif isinstance(self.extra, CreateDatasetEventExtraType0):
            extra = self.extra.to_dict()
        else:
            extra = self.extra

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset_uri": dataset_uri,
            }
        )
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_dataset_event_extra_type_0 import CreateDatasetEventExtraType0

        d = dict(src_dict)
        dataset_uri = d.pop("dataset_uri")

        def _parse_extra(data: object) -> CreateDatasetEventExtraType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_type_0 = CreateDatasetEventExtraType0.from_dict(data)

                return extra_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateDatasetEventExtraType0 | None | Unset, data)

        extra = _parse_extra(d.pop("extra", UNSET))

        create_dataset_event = cls(
            dataset_uri=dataset_uri,
            extra=extra,
        )

        create_dataset_event.additional_properties = d
        return create_dataset_event

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

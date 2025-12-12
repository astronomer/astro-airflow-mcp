from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DagWarning")


@_attrs_define
class DagWarning:
    """
    Attributes:
        dag_id (str | Unset): The dag_id.
        warning_type (str | Unset): The warning type for the dag warning.
        message (str | Unset): The message for the dag warning.
        timestamp (str | Unset): The time when this warning was logged.
    """

    dag_id: str | Unset = UNSET
    warning_type: str | Unset = UNSET
    message: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dag_id = self.dag_id

        warning_type = self.warning_type

        message = self.message

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if warning_type is not UNSET:
            field_dict["warning_type"] = warning_type
        if message is not UNSET:
            field_dict["message"] = message
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dag_id = d.pop("dag_id", UNSET)

        warning_type = d.pop("warning_type", UNSET)

        message = d.pop("message", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        dag_warning = cls(
            dag_id=dag_id,
            warning_type=warning_type,
            message=message,
            timestamp=timestamp,
        )

        dag_warning.additional_properties = d
        return dag_warning

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

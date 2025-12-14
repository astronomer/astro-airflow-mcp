from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_response_errors_item import BulkActionResponseErrorsItem


T = TypeVar("T", bound="BulkActionResponse")


@_attrs_define
class BulkActionResponse:
    """Serializer for individual bulk action responses.

    Represents the outcome of a single bulk operation (create, update, or delete).
    The response includes a list of successful keys and any errors encountered during the operation.
    This structure helps users understand which key actions succeeded and which failed.

        Attributes:
            success (list[str] | Unset): A list of unique id/key representing successful operations.
            errors (list[BulkActionResponseErrorsItem] | Unset): A list of errors encountered during the operation, each
                containing details about the issue.
    """

    success: list[str] | Unset = UNSET
    errors: list[BulkActionResponseErrorsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success: list[str] | Unset = UNSET
        if not isinstance(self.success, Unset):
            success = self.success

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_action_response_errors_item import BulkActionResponseErrorsItem

        d = dict(src_dict)
        success = cast(list[str], d.pop("success", UNSET))

        _errors = d.pop("errors", UNSET)
        errors: list[BulkActionResponseErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BulkActionResponseErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        bulk_action_response = cls(
            success=success,
            errors=errors,
        )

        bulk_action_response.additional_properties = d
        return bulk_action_response

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

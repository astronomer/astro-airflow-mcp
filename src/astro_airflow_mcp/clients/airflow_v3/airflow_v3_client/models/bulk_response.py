from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_response import BulkActionResponse


T = TypeVar("T", bound="BulkResponse")


@_attrs_define
class BulkResponse:
    """Serializer for responses to bulk entity operations.

    This represents the results of create, update, and delete actions performed on entity in bulk.
    Each action (if requested) is represented as a field containing details about successful keys and any encountered
    errors.
    Fields are populated in the response only if the respective action was part of the request, else are set None.

        Attributes:
            create (BulkActionResponse | None | Unset): Details of the bulk create operation, including successful keys and
                errors.
            update (BulkActionResponse | None | Unset): Details of the bulk update operation, including successful keys and
                errors.
            delete (BulkActionResponse | None | Unset): Details of the bulk delete operation, including successful keys and
                errors.
    """

    create: BulkActionResponse | None | Unset = UNSET
    update: BulkActionResponse | None | Unset = UNSET
    delete: BulkActionResponse | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_action_response import BulkActionResponse

        create: dict[str, Any] | None | Unset
        if isinstance(self.create, Unset):
            create = UNSET
        elif isinstance(self.create, BulkActionResponse):
            create = self.create.to_dict()
        else:
            create = self.create

        update: dict[str, Any] | None | Unset
        if isinstance(self.update, Unset):
            update = UNSET
        elif isinstance(self.update, BulkActionResponse):
            update = self.update.to_dict()
        else:
            update = self.update

        delete: dict[str, Any] | None | Unset
        if isinstance(self.delete, Unset):
            delete = UNSET
        elif isinstance(self.delete, BulkActionResponse):
            delete = self.delete.to_dict()
        else:
            delete = self.delete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create is not UNSET:
            field_dict["create"] = create
        if update is not UNSET:
            field_dict["update"] = update
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_action_response import BulkActionResponse

        d = dict(src_dict)

        def _parse_create(data: object) -> BulkActionResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                create_type_0 = BulkActionResponse.from_dict(data)

                return create_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BulkActionResponse | None | Unset, data)

        create = _parse_create(d.pop("create", UNSET))

        def _parse_update(data: object) -> BulkActionResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                update_type_0 = BulkActionResponse.from_dict(data)

                return update_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BulkActionResponse | None | Unset, data)

        update = _parse_update(d.pop("update", UNSET))

        def _parse_delete(data: object) -> BulkActionResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                delete_type_0 = BulkActionResponse.from_dict(data)

                return delete_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BulkActionResponse | None | Unset, data)

        delete = _parse_delete(d.pop("delete", UNSET))

        bulk_response = cls(
            create=create,
            update=update,
            delete=delete,
        )

        bulk_response.additional_properties = d
        return bulk_response

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

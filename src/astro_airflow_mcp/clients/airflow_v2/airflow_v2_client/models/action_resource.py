from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action
    from ..models.resource import Resource


T = TypeVar("T", bound="ActionResource")


@_attrs_define
class ActionResource:
    """The Action-Resource item.

    *New in version 2.1.0*

        Attributes:
            action (Action | Unset): An action Item.

                *New in version 2.1.0*
            resource (Resource | Unset): A resource on which permissions are granted.

                *New in version 2.1.0*
    """

    action: Action | Unset = UNSET
    resource: Resource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action import Action
        from ..models.resource import Resource

        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: Action | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = Action.from_dict(_action)

        _resource = d.pop("resource", UNSET)
        resource: Resource | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = Resource.from_dict(_resource)

        action_resource = cls(
            action=action,
            resource=resource,
        )

        action_resource.additional_properties = d
        return action_resource

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

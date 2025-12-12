from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_resource import ActionResource


T = TypeVar("T", bound="Role")


@_attrs_define
class Role:
    """a role item.

    *New in version 2.1.0*

        Attributes:
            name (str | Unset): The name of the role

                *Changed in version 2.3.0*&#58; A minimum character length requirement ('minLength') is added.
            actions (list[ActionResource] | Unset):
    """

    name: str | Unset = UNSET
    actions: list[ActionResource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_resource import ActionResource

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _actions = d.pop("actions", UNSET)
        actions: list[ActionResource] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = ActionResource.from_dict(actions_item_data)

                actions.append(actions_item)

        role = cls(
            name=name,
            actions=actions,
        )

        role.additional_properties = d
        return role

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

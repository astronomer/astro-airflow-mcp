from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action


T = TypeVar("T", bound="ActionCollection")


@_attrs_define
class ActionCollection:
    """A collection of actions.

    *New in version 2.1.0*

        Attributes:
            total_entries (int | Unset): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            actions (list[Action] | Unset):
    """

    total_entries: int | Unset = UNSET
    actions: list[Action] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_entries = self.total_entries

        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action import Action

        d = dict(src_dict)
        total_entries = d.pop("total_entries", UNSET)

        _actions = d.pop("actions", UNSET)
        actions: list[Action] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = Action.from_dict(actions_item_data)

                actions.append(actions_item)

        action_collection = cls(
            total_entries=total_entries,
            actions=actions,
        )

        action_collection.additional_properties = d
        return action_collection

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

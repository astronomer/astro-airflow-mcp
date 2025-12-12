from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.bulk_action_on_existence import BulkActionOnExistence
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.variable_body import VariableBody


T = TypeVar("T", bound="BulkCreateActionVariableBody")


@_attrs_define
class BulkCreateActionVariableBody:
    """
    Attributes:
        action (Literal['create']): The action to be performed on the entities.
        entities (list[VariableBody]): A list of entities to be created.
        action_on_existence (BulkActionOnExistence | Unset): Bulk Action to be taken if the entity already exists or
            not.
    """

    action: Literal["create"]
    entities: list[VariableBody]
    action_on_existence: BulkActionOnExistence | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        entities = []
        for entities_item_data in self.entities:
            entities_item = entities_item_data.to_dict()
            entities.append(entities_item)

        action_on_existence: str | Unset = UNSET
        if not isinstance(self.action_on_existence, Unset):
            action_on_existence = self.action_on_existence.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "entities": entities,
            }
        )
        if action_on_existence is not UNSET:
            field_dict["action_on_existence"] = action_on_existence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variable_body import VariableBody

        d = dict(src_dict)
        action = cast(Literal["create"], d.pop("action"))
        if action != "create":
            raise ValueError(f"action must match const 'create', got '{action}'")

        entities = []
        _entities = d.pop("entities")
        for entities_item_data in _entities:
            entities_item = VariableBody.from_dict(entities_item_data)

            entities.append(entities_item)

        _action_on_existence = d.pop("action_on_existence", UNSET)
        action_on_existence: BulkActionOnExistence | Unset
        if isinstance(_action_on_existence, Unset):
            action_on_existence = UNSET
        else:
            action_on_existence = BulkActionOnExistence(_action_on_existence)

        bulk_create_action_variable_body = cls(
            action=action,
            entities=entities,
            action_on_existence=action_on_existence,
        )

        return bulk_create_action_variable_body

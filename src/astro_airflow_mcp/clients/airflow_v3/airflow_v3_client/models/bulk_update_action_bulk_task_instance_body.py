from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.bulk_action_not_on_existence import BulkActionNotOnExistence
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_task_instance_body import BulkTaskInstanceBody


T = TypeVar("T", bound="BulkUpdateActionBulkTaskInstanceBody")


@_attrs_define
class BulkUpdateActionBulkTaskInstanceBody:
    """
    Attributes:
        action (Literal['update']): The action to be performed on the entities.
        entities (list[BulkTaskInstanceBody]): A list of entities to be updated.
        action_on_non_existence (BulkActionNotOnExistence | Unset): Bulk Action to be taken if the entity does not
            exist.
    """

    action: Literal["update"]
    entities: list[BulkTaskInstanceBody]
    action_on_non_existence: BulkActionNotOnExistence | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        entities = []
        for entities_item_data in self.entities:
            entities_item = entities_item_data.to_dict()
            entities.append(entities_item)

        action_on_non_existence: str | Unset = UNSET
        if not isinstance(self.action_on_non_existence, Unset):
            action_on_non_existence = self.action_on_non_existence.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "entities": entities,
            }
        )
        if action_on_non_existence is not UNSET:
            field_dict["action_on_non_existence"] = action_on_non_existence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_task_instance_body import BulkTaskInstanceBody

        d = dict(src_dict)
        action = cast(Literal["update"], d.pop("action"))
        if action != "update":
            raise ValueError(f"action must match const 'update', got '{action}'")

        entities = []
        _entities = d.pop("entities")
        for entities_item_data in _entities:
            entities_item = BulkTaskInstanceBody.from_dict(entities_item_data)

            entities.append(entities_item)

        _action_on_non_existence = d.pop("action_on_non_existence", UNSET)
        action_on_non_existence: BulkActionNotOnExistence | Unset
        if isinstance(_action_on_non_existence, Unset):
            action_on_non_existence = UNSET
        else:
            action_on_non_existence = BulkActionNotOnExistence(_action_on_non_existence)

        bulk_update_action_bulk_task_instance_body = cls(
            action=action,
            entities=entities,
            action_on_non_existence=action_on_non_existence,
        )

        return bulk_update_action_bulk_task_instance_body

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.bulk_action_not_on_existence import BulkActionNotOnExistence
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_task_instance_body import BulkTaskInstanceBody


T = TypeVar("T", bound="BulkDeleteActionPoolBody")


@_attrs_define
class BulkDeleteActionPoolBody:
    """
    Attributes:
        action (Literal['delete']): The action to be performed on the entities.
        entities (list[BulkTaskInstanceBody | str]): A list of entity id/key or entity objects to be deleted.
        action_on_non_existence (BulkActionNotOnExistence | Unset): Bulk Action to be taken if the entity does not
            exist.
    """

    action: Literal["delete"]
    entities: list[BulkTaskInstanceBody | str]
    action_on_non_existence: BulkActionNotOnExistence | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_task_instance_body import BulkTaskInstanceBody

        action = self.action

        entities = []
        for entities_item_data in self.entities:
            entities_item: dict[str, Any] | str
            if isinstance(entities_item_data, BulkTaskInstanceBody):
                entities_item = entities_item_data.to_dict()
            else:
                entities_item = entities_item_data
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
        action = cast(Literal["delete"], d.pop("action"))
        if action != "delete":
            raise ValueError(f"action must match const 'delete', got '{action}'")

        entities = []
        _entities = d.pop("entities")
        for entities_item_data in _entities:

            def _parse_entities_item(data: object) -> BulkTaskInstanceBody | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entities_item_type_1 = BulkTaskInstanceBody.from_dict(data)

                    return entities_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(BulkTaskInstanceBody | str, data)

            entities_item = _parse_entities_item(entities_item_data)

            entities.append(entities_item)

        _action_on_non_existence = d.pop("action_on_non_existence", UNSET)
        action_on_non_existence: BulkActionNotOnExistence | Unset
        if isinstance(_action_on_non_existence, Unset):
            action_on_non_existence = UNSET
        else:
            action_on_non_existence = BulkActionNotOnExistence(_action_on_non_existence)

        bulk_delete_action_pool_body = cls(
            action=action,
            entities=entities,
            action_on_non_existence=action_on_non_existence,
        )

        return bulk_delete_action_pool_body

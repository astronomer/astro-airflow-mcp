from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.bulk_create_action_variable_body import BulkCreateActionVariableBody
    from ..models.bulk_delete_action_variable_body import BulkDeleteActionVariableBody
    from ..models.bulk_update_action_variable_body import BulkUpdateActionVariableBody


T = TypeVar("T", bound="BulkBodyVariableBody")


@_attrs_define
class BulkBodyVariableBody:
    """
    Attributes:
        actions (list[BulkCreateActionVariableBody | BulkDeleteActionVariableBody | BulkUpdateActionVariableBody]):
    """

    actions: list[BulkCreateActionVariableBody | BulkDeleteActionVariableBody | BulkUpdateActionVariableBody]

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_create_action_variable_body import BulkCreateActionVariableBody
        from ..models.bulk_update_action_variable_body import BulkUpdateActionVariableBody

        actions = []
        for actions_item_data in self.actions:
            actions_item: dict[str, Any]
            if isinstance(actions_item_data, BulkCreateActionVariableBody):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, BulkUpdateActionVariableBody):
                actions_item = actions_item_data.to_dict()
            else:
                actions_item = actions_item_data.to_dict()

            actions.append(actions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "actions": actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_create_action_variable_body import BulkCreateActionVariableBody
        from ..models.bulk_delete_action_variable_body import BulkDeleteActionVariableBody
        from ..models.bulk_update_action_variable_body import BulkUpdateActionVariableBody

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:

            def _parse_actions_item(
                data: object,
            ) -> BulkCreateActionVariableBody | BulkDeleteActionVariableBody | BulkUpdateActionVariableBody:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_0 = BulkCreateActionVariableBody.from_dict(data)

                    return actions_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_1 = BulkUpdateActionVariableBody.from_dict(data)

                    return actions_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                actions_item_type_2 = BulkDeleteActionVariableBody.from_dict(data)

                return actions_item_type_2

            actions_item = _parse_actions_item(actions_item_data)

            actions.append(actions_item)

        bulk_body_variable_body = cls(
            actions=actions,
        )

        return bulk_body_variable_body

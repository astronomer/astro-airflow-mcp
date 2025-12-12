from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.bulk_create_action_connection_body import BulkCreateActionConnectionBody
    from ..models.bulk_delete_action_connection_body import BulkDeleteActionConnectionBody
    from ..models.bulk_update_action_connection_body import BulkUpdateActionConnectionBody


T = TypeVar("T", bound="BulkBodyConnectionBody")


@_attrs_define
class BulkBodyConnectionBody:
    """
    Attributes:
        actions (list[BulkCreateActionConnectionBody | BulkDeleteActionConnectionBody |
            BulkUpdateActionConnectionBody]):
    """

    actions: list[BulkCreateActionConnectionBody | BulkDeleteActionConnectionBody | BulkUpdateActionConnectionBody]

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_create_action_connection_body import BulkCreateActionConnectionBody
        from ..models.bulk_update_action_connection_body import BulkUpdateActionConnectionBody

        actions = []
        for actions_item_data in self.actions:
            actions_item: dict[str, Any]
            if isinstance(actions_item_data, BulkCreateActionConnectionBody):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, BulkUpdateActionConnectionBody):
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
        from ..models.bulk_create_action_connection_body import BulkCreateActionConnectionBody
        from ..models.bulk_delete_action_connection_body import BulkDeleteActionConnectionBody
        from ..models.bulk_update_action_connection_body import BulkUpdateActionConnectionBody

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:

            def _parse_actions_item(
                data: object,
            ) -> BulkCreateActionConnectionBody | BulkDeleteActionConnectionBody | BulkUpdateActionConnectionBody:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_0 = BulkCreateActionConnectionBody.from_dict(data)

                    return actions_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_1 = BulkUpdateActionConnectionBody.from_dict(data)

                    return actions_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                actions_item_type_2 = BulkDeleteActionConnectionBody.from_dict(data)

                return actions_item_type_2

            actions_item = _parse_actions_item(actions_item_data)

            actions.append(actions_item)

        bulk_body_connection_body = cls(
            actions=actions,
        )

        return bulk_body_connection_body

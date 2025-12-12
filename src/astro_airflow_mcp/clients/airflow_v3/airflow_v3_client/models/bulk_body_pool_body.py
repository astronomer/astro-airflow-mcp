from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.bulk_create_action_pool_body import BulkCreateActionPoolBody
    from ..models.bulk_delete_action_pool_body import BulkDeleteActionPoolBody
    from ..models.bulk_update_action_pool_body import BulkUpdateActionPoolBody


T = TypeVar("T", bound="BulkBodyPoolBody")


@_attrs_define
class BulkBodyPoolBody:
    """
    Attributes:
        actions (list[BulkCreateActionPoolBody | BulkDeleteActionPoolBody | BulkUpdateActionPoolBody]):
    """

    actions: list[BulkCreateActionPoolBody | BulkDeleteActionPoolBody | BulkUpdateActionPoolBody]

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_create_action_pool_body import BulkCreateActionPoolBody
        from ..models.bulk_update_action_pool_body import BulkUpdateActionPoolBody

        actions = []
        for actions_item_data in self.actions:
            actions_item: dict[str, Any]
            if isinstance(actions_item_data, BulkCreateActionPoolBody):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, BulkUpdateActionPoolBody):
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
        from ..models.bulk_create_action_pool_body import BulkCreateActionPoolBody
        from ..models.bulk_delete_action_pool_body import BulkDeleteActionPoolBody
        from ..models.bulk_update_action_pool_body import BulkUpdateActionPoolBody

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:

            def _parse_actions_item(
                data: object,
            ) -> BulkCreateActionPoolBody | BulkDeleteActionPoolBody | BulkUpdateActionPoolBody:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_0 = BulkCreateActionPoolBody.from_dict(data)

                    return actions_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_1 = BulkUpdateActionPoolBody.from_dict(data)

                    return actions_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                actions_item_type_2 = BulkDeleteActionPoolBody.from_dict(data)

                return actions_item_type_2

            actions_item = _parse_actions_item(actions_item_data)

            actions.append(actions_item)

        bulk_body_pool_body = cls(
            actions=actions,
        )

        return bulk_body_pool_body

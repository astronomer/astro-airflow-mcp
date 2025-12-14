from enum import Enum


class DagWarningType(str, Enum):
    ASSET_CONFLICT = "asset conflict"
    NON_EXISTENT_POOL = "non-existent pool"

    def __str__(self) -> str:
        return str(self.value)

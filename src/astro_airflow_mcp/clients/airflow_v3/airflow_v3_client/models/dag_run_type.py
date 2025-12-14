from enum import Enum


class DagRunType(str, Enum):
    ASSET_TRIGGERED = "asset_triggered"
    BACKFILL = "backfill"
    MANUAL = "manual"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class DAGRunRunType(str, Enum):
    BACKFILL = "backfill"
    DATASET_TRIGGERED = "dataset_triggered"
    MANUAL = "manual"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)

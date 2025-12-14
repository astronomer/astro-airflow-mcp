from enum import Enum


class ReprocessBehavior(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)

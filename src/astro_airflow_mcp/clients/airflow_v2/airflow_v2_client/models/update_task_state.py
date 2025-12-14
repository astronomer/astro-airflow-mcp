from enum import Enum


class UpdateTaskState(str, Enum):
    FAILED = "failed"
    SKIPPED = "skipped"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)

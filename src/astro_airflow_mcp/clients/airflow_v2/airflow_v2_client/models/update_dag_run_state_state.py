from enum import Enum


class UpdateDagRunStateState(str, Enum):
    FAILED = "failed"
    QUEUED = "queued"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)

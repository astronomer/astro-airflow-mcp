from enum import Enum


class ExternalViewResponseDestination(str, Enum):
    DAG = "dag"
    DAG_RUN = "dag_run"
    NAV = "nav"
    TASK = "task"
    TASK_INSTANCE = "task_instance"

    def __str__(self) -> str:
        return str(self.value)

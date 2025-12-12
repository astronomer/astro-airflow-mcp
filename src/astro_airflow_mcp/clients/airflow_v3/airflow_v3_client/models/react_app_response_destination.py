from enum import Enum


class ReactAppResponseDestination(str, Enum):
    DAG = "dag"
    DAG_RUN = "dag_run"
    DASHBOARD = "dashboard"
    NAV = "nav"
    TASK = "task"
    TASK_INSTANCE = "task_instance"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class TriggerRule(str, Enum):
    ALL_DONE = "all_done"
    ALL_DONE_SETUP_SUCCESS = "all_done_setup_success"
    ALL_FAILED = "all_failed"
    ALL_SKIPPED = "all_skipped"
    ALL_SUCCESS = "all_success"
    ALWAYS = "always"
    DUMMY = "dummy"
    NONE_FAILED = "none_failed"
    NONE_FAILED_MIN_ONE_SUCCESS = "none_failed_min_one_success"
    NONE_FAILED_OR_SKIPPED = "none_failed_or_skipped"
    NONE_SKIPPED = "none_skipped"
    ONE_DONE = "one_done"
    ONE_FAILED = "one_failed"
    ONE_SUCCESS = "one_success"

    def __str__(self) -> str:
        return str(self.value)

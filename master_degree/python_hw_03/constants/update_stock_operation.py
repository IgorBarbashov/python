from enum import Enum


class UpdateStockOperation(str, Enum):
    ADD = "add"
    REMOVE = "remove"

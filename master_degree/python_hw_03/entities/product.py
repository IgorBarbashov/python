from __future__ import annotations
from typeguard import typechecked

from constants.update_stock_operation import UpdateStockOperation
from exceptions.product import NegativeProductQuantityError


@typechecked
class Product:

    __slots__ = ("__name", "__price", "__stock")

    def __init__(self, name: str, price: float, stock: int) -> None:
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity: int, operation: UpdateStockOperation) -> None:
        updated_stock = self.__stock

        if operation is UpdateStockOperation.ADD:
            updated_stock += quantity
        elif operation is UpdateStockOperation.REMOVE:
            updated_stock -= quantity

        if updated_stock < 0:
            raise NegativeProductQuantityError(
                f"Попытка списания {quantity} единиц при остатке {self.__stock}")

        self.__stock = updated_stock

    def __repr__(self) -> str:
        return f"Product(name={self.__name!r}, price={self.__price:.2f}, stock={self.__stock})"

    def __eq__(self, other: Product) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.__name == other.__name and self.__price == other.__price

    def __hash__(self) -> int:
        return hash((self.__name, self.__price))

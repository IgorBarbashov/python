from typing import Self
from typeguard import typechecked

from .product import Product
from .order import Order
from utils.singleton import Singleton
from exceptions.product import ProductAlreadyExistsError


@Singleton
@typechecked
class Store:

    __slots__ = ("__products", "__order_factory")

    def __init__(self, order_factory: type[Order] = Order) -> None:
        self.__products: list[Product] = []
        self.__order_factory = order_factory

    def add_product(self, product: Product) -> Self:
        if product in self.__products:
            raise ProductAlreadyExistsError(
                f"Продукт {product.name} с ценой {product.price} уже присутствует на складе")

        self.__products.append(product)
        return self

    def list_products(self) -> str:
        if not self.__products:
            return "Склад пуст"

        header = "Продукты на складе:"
        lines = (f"- {product}" for product in self.__products)
        return "\n".join((header, *lines))

    def create_order(self) -> Order:
        return self.__order_factory()

    def __repr__(self) -> str:
        return (f"Store items={self.__products})")

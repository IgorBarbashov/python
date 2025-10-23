from typing import Self
from typeguard import typechecked

from .product import Product
from constants.update_stock_operation import UpdateStockOperation
from exceptions.product import NotEnoughProductError, ProductNotExistsError


@typechecked
class Order:

    __slots__ = ("__products",)

    def __init__(self) -> None:
        self.__products: dict[Product, int] = {}

    def add_product(self, product: Product, quantity: int) -> Self:
        if product.stock < quantity:
            raise NotEnoughProductError(
                f"Попытка добавить в заказ {quantity} товара, при наличии на складе {product.stock}")

        self.__products[product] = self.__products.get(product, 0) + quantity
        product.update_stock(quantity, UpdateStockOperation.REMOVE)

        return self

    def remove_product(self, product: Product, quantity: int) -> Self:
        self.__is_product_exists(product)

        updated_quantity = self.__products[product] - quantity
        if updated_quantity > 0:
            self.__products[product] = updated_quantity
        else:
            del self.__products[product]

        return self

    def return_product(self, product: Product, quantity: int) -> Self:
        self.__is_product_exists(product)

        quantity_to_return = min(self.__products[product], quantity)
        product.update_stock(quantity_to_return, UpdateStockOperation.ADD)

        return self.remove_product(product, quantity_to_return)

    def calculate_total(self) -> float:
        return sum(product.price * quantity for product, quantity in self.__products.items())

    def __repr__(self) -> str:
        return (
            f"Order(total={self.calculate_total():.2f}, "
            f"items={self.__products})"
        )

    def __is_product_exists(self, product: Product) -> bool:
        if product not in self.__products:
            raise ProductNotExistsError(
                f"Продукта {product.name} нет в заказе")

        return True

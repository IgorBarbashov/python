class ProductError(Exception):
    def __init__(self, message):
        super().__init__(f"Ошибка при работе с товаром: {message}")


class NegativeProductQuantityError(ProductError):
    def __init__(self, message="Количество товара не может быть меньше нуля"):
        super().__init__(message)


class NotEnoughProductError(ProductError):
    def __init__(self, message="Недостаточное количество товара"):
        super().__init__(message)


class ProductAlreadyExistsError(ProductError):
    def __init__(self, message="Продукт уже присутствует на складе"):
        super().__init__(message)


class ProductNotExistsError(ProductError):
    def __init__(self, message="Такого продукта нет в заказе"):
        super().__init__(message)

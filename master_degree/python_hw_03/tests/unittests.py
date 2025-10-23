import unittest

from entities.store import Store
from entities.product import Product
from exceptions.product import NotEnoughProductError, ProductNotExistsError


class TestStoreOrderProduct(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.product1 = Product("Ноутбук", 1000, 5)
        self.product2 = Product("Смартфон", 500, 10)
        self.store.add_product(self.product1)
        self.store.add_product(self.product2)

    def test_store_add_and_list_products(self):
        products_list = self.store.list_products()

        self.assertIn("Ноутбук", products_list)
        self.assertIn("Смартфон", products_list)
        self.assertIn("stock=5", products_list)
        self.assertIn("stock=10", products_list)

    def test_order_add_and_stock_update(self):
        order = self.store.create_order()
        order.add_product(self.product1, 2)
        order.add_product(self.product2, 3)

        self.assertEqual(self.product1.stock, 3)
        self.assertEqual(self.product2.stock, 7)
        self.assertEqual(order.calculate_total(), 3500)

    def test_order_remove_product(self):
        order = self.store.create_order()
        order.add_product(self.product1, 3)
        order.remove_product(self.product1, 2)

        self.assertEqual(order.calculate_total(), 1000)
        self.assertIn(self.product1, order._Order__products)
        order.remove_product(self.product1, 1)
        self.assertNotIn(self.product1, order._Order__products)

    def test_order_return_product_and_stock(self):
        order = self.store.create_order()
        order.add_product(self.product2, 5)
        order.return_product(self.product2, 3)

        self.assertEqual(self.product2.stock, 8)
        self.assertEqual(order._Order__products[self.product2], 2)
        order.return_product(self.product2, 2)
        self.assertNotIn(self.product2, order._Order__products)

    def test_add_product_not_enough_stock(self):
        order = self.store.create_order()
        with self.assertRaises(NotEnoughProductError):
            order.add_product(self.product1, 6)

    def test_return_nonexistent_product(self):
        order = self.store.create_order()
        with self.assertRaises(ProductNotExistsError):
            order.return_product(self.product1, 1)

    def test_remove_nonexistent_product(self):
        order = self.store.create_order()
        with self.assertRaises(ProductNotExistsError):
            order.remove_product(self.product1, 1)

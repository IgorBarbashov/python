from __future__ import annotations
from typing import NoReturn


class Book:
    def __init__(self, title: str, author: str) -> NoReturn:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"{self.author - self.title}"

    # класс-метод, первый аргумент - конструктор класса
    @classmethod
    def from_string(cls, input_string: str) -> Book: # чтобы здесь могли ссылаться на свой же класс, используем бибилотеку __future__
        title, author = input_string.split(" - ")
        return cls(title, author)

    # статический метод, не принимает ни self, ни cls
    @staticmethod
    def in_isbn(input: str) -> bool:
        return len(input) == 13


book = Book("Harry Potter", "J. Rouling")

new_book = book.from_string("A - B")

print(Book.in_isbn("123"))

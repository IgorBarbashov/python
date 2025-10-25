from pydantic import BaseModel, EmailStr
from typing import Optional


class BookModel(BaseModel):
    title: str
    author: str
    year: int
    available: bool


class UserModel(BaseModel):
    name: str
    email: EmailStr
    membership_id: str


# Возможная реализация функций


library: list[BookModel] = []


def add_book(title: str, author: str, year: int, available: bool = True) -> BookModel:
    book = BookModel(title=title, author=author,
                     year=year, available=available)
    library.append(book)
    return book


def find_book(title: str) -> Optional[BookModel]:
    for book in library:
        if book.title.lower() == title.lower():
            return book
    return None


def is_book_borrow(title: str) -> bool:
    book = find_book(title)
    if book is None:
        return False
    return not book.available


def return_book(title: str) -> bool:
    book = find_book(title)
    if book is None or book.available == True:
        return False
    book.available = True
    return True

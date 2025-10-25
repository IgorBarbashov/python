from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List


class BookModel(BaseModel):
    title: str
    author: str
    year: int
    available: bool
    categories: List[str] = Field(default_factory=list)

    @field_validator('categories')
    @classmethod
    def validate_categories(cls, categories: List[str]) -> List[str]:
        if not categories:
            raise ValueError('Книга должна иметь хотя бы одну категорию')

        if any(not category.strip() for category in categories):
            raise ValueError('Категории не могут быть пустыми строками')

        categories_without_doubles = list(dict.fromkeys(
            cat.strip().lower() for cat in categories))
        return categories_without_doubles


class UserModel(BaseModel):
    name: str
    email: EmailStr
    membership_id: str


class LibraryModel(BaseModel):
    books: List[BookModel] = Field(default_factory=list)
    users: List[UserModel] = Field(default_factory=list)

    def total_books(self) -> int:
        return len(self.books)

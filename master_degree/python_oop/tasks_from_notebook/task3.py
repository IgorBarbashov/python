# Строки в Python сравниваются на основе значений символов
# Т. е. если мы захотим выяснить, что больше, «Apple» или «Яблоко», то «Яблоко» окажется больше
# А всё потому, что английская буква A имеет значение 65 (берётся из таблицы кодировки), а русская буква Я – 1 071 (это можно выяснить с помощью функции ord())
# Реализуйте класс RealString так, чтобы можно было сравнивать между собой как объекты класса, так и обычные строки с экземплярами класса RealString
# Все нужные магические методы мы прошли

from __future__ import annotations
from functools import total_ordering
from typing import NoReturn

@total_ordering
class RealString:

  def __init__(self, string: str) -> NoReturn:
    self.string = string
  
  def __str__(self) -> str:
    return self.string
  
  @staticmethod
  def get_real_string(value: str | RealString) -> str:
    return value.string if isinstance(value, RealString) else value

  def __eq__(self, value: str | RealString) -> bool:
    real_string = RealString.get_real_string(value)
    return self.string == real_string
  
  def __lt__(self, value: str | RealString) -> bool:
    real_string = RealString.get_real_string(value)
    return self.string < real_string


if __name__ == "__main__":
  print("Сравнение объектов")
  string_a = RealString("Apple")
  string_b = RealString("Яблоко")
  string_c = RealString("Apple")
  print(f"{string_a} == {string_b}:", string_a == string_b)
  print(f"{string_a} == {string_c}:", string_a == string_c)
  print(f"{string_b} == {string_c}:", string_b == string_c)
  print(f"{string_b} < {string_c}:", string_b < string_c)
  print(f"{string_b} > {string_c}:", string_b > string_c)

  print()
  print("Сравнение объектов и строк")
  string_d = "Apple"
  string_e = "Яблоко"
  print(f"{string_a} == {string_d}:", string_a == string_d)
  print(f"{string_a} == {string_e}:", string_a == string_e)
  print(f"{string_a} < {string_d}:", string_a < string_d)
  print(f"{string_a} <= {string_d}:", string_a <= string_d)
  print(f"{string_a} > {string_e}:", string_a > string_e)

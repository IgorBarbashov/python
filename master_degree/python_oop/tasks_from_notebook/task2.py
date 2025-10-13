# Построить треугольник из отрезков можно лишь при одном условии: сумма длин двух любых сторон всегда больше длины третьей стороны
# Необходимо реализовать класс TriangleExist, принимающий длину отрезков, из которых состоит треугольник.
# При создании экземпляра нужно проверять, возможен ли такой треугольник
# case 1: Да -> Треугольник возможен
# case 2: Нет -> Треугольник построить не получится

from typing import NoReturn


class TriangleExist:
  def __init__(self, a: float, b: float, c: float) -> NoReturn:
    self.a = a
    self.b = b
    self.c = c

  def check_lines(self) -> bool:
    return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

  def is_triangle_exists(self) -> str:
    if self.check_lines():
      return "Да -> Треугольник возможен"
    else:
      return "Нет -> Треугольник построить не получится"


if __name__ == "__main__":
  triangle_1 = TriangleExist(1, 2.5, 3)
  is_triangle_exists_1 = triangle_1.is_triangle_exists()
  print(is_triangle_exists_1)

  triangle_2 = TriangleExist(1, 2, 3)
  is_triangle_exists_2 = triangle_2.is_triangle_exists()
  print(is_triangle_exists_2)

# Создайте класс SparkleWater для определения типа газированной воды, принимающий 1 аргумент при инициализации -
# что мы добавим в газированную воду, чтобы получить свой уникальный напиток
# В этом классе необходимо реализовать метод show_the_drink(), выводящий пользователю
# «Газировка с {arg}» при наличии добавки, а иначе должна отобразиться фраза: «Обычная газированная вода»

from typing import NoReturn

class SparkleWater:
  def __init__(self, addon: str | None = None) -> NoReturn:
    self.addon = addon
  
  def show_the_drink(self):
    if self.addon == None:
      print("Обычная газированная вода")
    else:
      print(f"Газировка с {self.addon}")

if __name__ == "__main__":
  clear_soda = SparkleWater()
  clear_soda.show_the_drink()

  soda_with_strawberry = SparkleWater("клубника")
  soda_with_strawberry.show_the_drink()

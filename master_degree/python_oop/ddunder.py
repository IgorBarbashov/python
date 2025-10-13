class Animal:
    def __init__(self, color, age):
      self.age = age
      self.color = color

    # Используется если __str__() не определен
    def __repr__(self):
      return f"This is Animal with age = {self.age} and color = {self.color}"

    # Если определен, то отвечает за строковое представление объекта класса
    def __str__(self):
       return f"Age {self.age}"

    def eat(self):
        print("Я могу есть")

    def sleep(self):
        print("Я могу спать")

    def animal_birthday(self):
      self.age += 1


cat = Animal("black", 2)


# Если не определены ни __str__(), ни __repr()__, то используется стандартное строковое представление
print(cat) # "Age 2", если определен __str__()
print(cat) # "This is Animal with age = 2 and color = black", если есть __repr__() и нет __str__()
print(cat) # "<__main__.Animal object at 0x0000018FEC4160C0>", если нет ни __repr__(), ни __str__()

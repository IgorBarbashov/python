
class Singletone:

    _instance = None # статическое поле класса

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:

            # такая конструкция обусловлена множественным наследованием в python
            # super(Singletone, cls) - найди следующий класс в иерархии после Singletone для класса cls и работай с ним, как с родителем
            # __new__(cls) - вызывается метод родителского класса, ему передается класс cls, в итоге получаем instance класса cls,
            # созданный с учетом всех правил множественного наследования python
            # если как-то жестко привязываться, типа: object.__new(cls)__ - то можно поломать цепочку наследования
            cls._instance = super(Singletone, cls).__new__(cls)

        return cls._instance

s1 = Singletone(2, 3)
s2 = Singletone()
s1.value = 10

print(s1.value)
print(s2.value)
print(s1 == s2)


# --------------------------------------------------


class Singletone:

    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singletone, cls).__new__(cls)
        return cls._instance
    
    # добавляется метод __init__ для инициализации полей instanse'а
    def __init__(self, value):

        # без этой проверки значение value будет перезаписываться, т.к. __init__ вызывается при каждом вызове конструктора класса
        # а т.к. Singletone всегда возвращает один и тот же объект, то поле будет перезаписываться
        # данная проверка разрещает инициализацию поля только при првом вызове
        if not hasattr(self, "_init"):
            self.value = value
            self._init = True
    

s1 = Singletone(10)
s2 = Singletone(20)

print(s1.value)
print(s2.value)

print(id(s1))
print(id(s2))
print(id(s2) == id(s1))

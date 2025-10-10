try:
    from math import sqrt
except ImportError:
    print("Ошибка: не удалось импортировать модуль math")
else:
    class NegativeNumberError(Exception):
        def __init__(self):
            self.message = f"Ошибка: нельзя извлечь квадратный корень из отрицательноого числа"
            super().__init__(self.message)


    def validate_value(value):
        if value < 0:
            raise NegativeNumberError()


    def main():
        try:
            value = int(input("Введите целое число: "))
            validate_value(value)
            result = sqrt(int(value))
            print(f"Квадратный корень из числа {value} = {result}")
        except NegativeNumberError as e:
            print(e)
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")


    if __name__ == "__main__":
        main()

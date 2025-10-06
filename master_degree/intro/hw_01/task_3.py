class NumberError(Exception):
    def __init__(self, msg = "некорректное"):
        self.message = f"Ошибка: в списке присутствует {msg} число"
        super().__init__(self.message)


class EvenNumberError(NumberError):
    def __init__(self):
        super().__init__("четное")


class NegativeNumberError(NumberError):
    def __init__(self):
        super().__init__("отрицательное")


def validate_value(value):
    if value < 0:
        raise NegativeNumberError()

    if value % 2 == 0:
        raise EvenNumberError()
    
    return True


def main():
    values = map(int, input("Введите целые числа через пробел: ").split(" "))
    result = 0

    try:
        for value in values:
            validate_value(value)
            result += value
    except (NumberError, NegativeNumberError, EvenNumberError) as e:
        print(e)
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
    else:
        print("Сумма чисел в списке:", result)


if __name__ == "__main__":
    main()

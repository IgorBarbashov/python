def main():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a / b
    except ValueError:
        print("Ошибка: введенные значение должно быть числами")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
    else:
        print("Результат деления:", result)


if __name__ == "__main__":
    main()

def main():
    string = input("Введите строку для преобразования: ")

    try:
        result = float(string)
        print(f"Число, полученное преобразованием из строки {result}")
    except ValueError:
        print("Ошибка: невозможно преобразовать введенную строку в число")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()

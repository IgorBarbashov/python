def main():
    values = list(input("Введите элеметы списка через пробел: ").split(" "))
    index = int(input(f"Введите индекс искомого элемента (от 0 до {len(values) - 1}): "))

    try:
        print(f"Элемент с индексом {index}: {values[index]}")
    except IndexError:
        print(f"Ошибка: элемента с индексом {index} не существует")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()

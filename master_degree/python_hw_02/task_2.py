source_filename = "prices.txt"

def main():
    try:
        with open(source_filename, "r", encoding="utf-8") as f:
            amount = 0

            for line in f:
                amount += int(line.split("\t")[-1])
            
            print(f"Общая стоимость заказа: {amount}")
    except FileNotFoundError:
        print(f"Ошибка: файл {source_filename} не найден")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()

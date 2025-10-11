source_filename = "source.txt"
destination_filename = "destination.txt"

def main():
    try:
        with open(source_filename, "r") as sf:
            with open(destination_filename, "w") as df:
                for line in sf:
                    df.write(line)
    except FileNotFoundError:
        print(f"Ошибка: файл {source_filename} не найден")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
    else:
        print(f"Файл {source_filename} скопирован в файл {destination_filename}")


if __name__ == "__main__":
    main()

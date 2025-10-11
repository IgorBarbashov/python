source_filename = "input.txt"
destination_filename = "unique_output.txt"

def main():
    try:
        with open(source_filename, "r") as sf:
            with open(destination_filename, "w") as df:
                uniq_lines = set()

                for line in sf:
                    if line not in uniq_lines:
                        df.write(line)
                        uniq_lines.add(line)
    except FileNotFoundError:
        print(f"Ошибка: файл {source_filename} не найден")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
    else:
        print(f"Уникальные строки из файла {source_filename} скопированы в файл {destination_filename}")


if __name__ == "__main__":
    main()

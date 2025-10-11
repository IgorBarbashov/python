import re

source_filename = "text_file.txt"

def main():
    try:
        with open(source_filename, "r", encoding="utf-8") as f:
            word_count = 0

            for line in f:
                clear_string = re.sub(r"[^\w ]", "", line, flags=re.UNICODE)
                word_count += len(clear_string.split())

            print(f"Количество слов в файле: {word_count}")
    except FileNotFoundError:
        print(f"Ошибка: файл {source_filename} не найден")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()

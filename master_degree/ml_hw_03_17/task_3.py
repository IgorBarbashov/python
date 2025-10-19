from typing import Tuple

default_app_name = "Блокнот"

file_types = {
    "pdf": "Adobe Acrobat",
    "docx": "Microsoft Word",
    "tar.gz": "WinRAR",
    "gz": "7-zip",
    "7z": "7-zip",
}

def get_app(file_type: str) -> str:
    return default_app_name if not file_type in file_types.keys() else file_types[file_type]


def is_count(value: str) -> bool:
    try:
        return True if int(value) and not value.startswith("0") else False
    except:
        return False


def split_to_name_and_ext(filename: str) -> Tuple[str, str]:
    name, *ext = filename.split(".")
    return (name, ".".join(ext))


def split_to_main_and_order(name: str) -> Tuple[str, int]:
    if not "_" in name:
        return (name, 1)

    first, *other, last = name.split("_")

    if not is_count(last):
        return (name, 1)
    
    return ("_".join([first] + other), int(last) + 1)


if __name__ == "__main__":
    filename = input()

    name, ext = split_to_name_and_ext(filename)
    main, order = split_to_main_and_order(name)
    app = get_app(ext)

    print(f"{main}_{order}.{ext}")
    print(app)

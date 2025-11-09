def double_print(string: str):
    if string == "":
        raise ValueError("empty string is not allowed")

    print(string)
    print(string)


double_print("")

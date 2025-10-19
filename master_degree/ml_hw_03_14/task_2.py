def last_discharge(a: str) -> int | float:
    n = a.split(".")
    return int(a) - 1 if len(n) == 1 else float(a) - 10 ** (0 - len(n[1]))

if __name__ == "__main__":
    n = input()
    print(last_discharge(n))

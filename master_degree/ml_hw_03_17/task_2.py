from typing import List, Tuple, NewType

CustomList = NewType('CustomList', List[Tuple[int, str]])

def get_list() -> CustomList:
    return [(int(x), y) for product in input().split(", ") for x, y in [product.split(" ")]]

def sort_list(list: CustomList) -> CustomList:
    return sorted(list, key=lambda x: (x[0], x[1]))

def print_list(list: CustomList):
    print(", ".join([f"{tup[0]} {tup[1]}" for tup in list]))


if __name__ == "__main__":
    list_1 = set(get_list())
    list_2 = set(get_list())
    
    list_new = list_1 & list_2
    list_1 = list_1 ^ list_new
    list_2 = list_2 ^ list_new

    print_list(sort_list(list_new))
    print_list(sort_list(list_1))
    print_list(sort_list(list_2))

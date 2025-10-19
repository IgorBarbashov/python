from typing import List

def is_odd(n: int) -> bool:
    return n % 2 != 0

def get_mediana(moneys: List[int]) -> float:
    sorted_moneys = sorted(moneys)
    moneys_count = len(sorted_moneys)

    if is_odd(moneys_count):
        return sorted_moneys[(moneys_count - 1) // 2]
    
    return (sorted_moneys[moneys_count // 2] + sorted_moneys[moneys_count // 2 - 1]) / 2


if __name__ == "__main__":
    n = int(input())
    silver = []
    gold = []
    
    for i in range(n):
        s, g = map(int, input().split())
        silver.append(s)
        gold.append(g)

    mediana_silver = get_mediana(silver)
    mediana_gold = get_mediana(gold)
    mediana_all = get_mediana(silver + gold)

    print(mediana_silver)
    print(mediana_gold)
    print(mediana_all)

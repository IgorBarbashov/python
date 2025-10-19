n = int(input())

if n < 1:
    print("ошибка")
    exit()

result = 0

for i in range(n + 1):
    if i % 15 == 0:
        continue

    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)

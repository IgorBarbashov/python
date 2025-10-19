s = input()

for c in s:
    if c.isdigit():
        print(c)
        break
else:
    print("нет")

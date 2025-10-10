n = int(input())
data = [list(map(int, input().split())) for i in range(n)]

for x in sorted(data, key=lambda x: -x[1]):
    print(x[0])

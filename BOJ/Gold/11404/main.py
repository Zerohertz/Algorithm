import sys

read = sys.stdin.readline

n = int(read())
m = int(read())

INF = 100_000_000
res = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, read().split())
    res[a - 1][b - 1] = min(res[a - 1][b - 1], c)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j != k:
                res[j][k] = min(res[j][k], res[j][i] + res[i][k])

for i in res:
    for j in i:
        if j == INF:
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()

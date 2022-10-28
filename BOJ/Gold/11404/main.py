import sys
read = sys.stdin.readline

n = int(read())
m = int(read())

res = [[100_001 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, read().split())
    if res[a - 1][b - 1] > c:
        res[a - 1][b - 1] = c

for i in range(n):
    for j in range(n):
        if i == j:
            res[i][j] = 0
        for k in range(n):
            if i != j:
                res[j][k] = min(res[j][k], res[j][i] + res[i][k])

for i in res:
    for j in i:
        print(j, end=' ')
    print()
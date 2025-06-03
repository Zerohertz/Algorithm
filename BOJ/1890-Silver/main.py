import sys

read = sys.stdin.readline

N = int(read())
l = [[0 for _ in range(N)] for _ in range(N)]
res = [[0 for _ in range(N)] for _ in range(N)]
res[0][0] = 1

for i in range(N):
    l[i] = list(map(int, read().split()))

for x in range(N):
    for y in range(N):
        n = l[x][y]
        if x == N - 1 and y == N - 1:
            break
        if 0 <= x + n < N:
            res[x + n][y] += res[x][y]
        if 0 <= y + n < N:
            res[x][y + n] += res[x][y]

print(res[-1][-1])

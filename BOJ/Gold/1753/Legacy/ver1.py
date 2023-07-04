import sys

read = sys.stdin.readline
INF = 100

V, E = map(int, read().split())
K = int(read())

g = [[INF for _ in range(V)] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, read().split())
    g[u - 1][v - 1] = w

d = [INF for _ in range(V)]
d[K - 1] = 0

for i in range(V):
    for j in range(V):
        d[j] = min(d[j], d[i] + g[i][j])

for i in d:
    if i == INF:
        print('INF')
    else:
        print(i)

import heapq
import sys

read = sys.stdin.readline

N = int(read())
M = int(read())
h = []
g = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, read().split())
    g[a - 1].append((b - 1, c))

start, end = map(int, read().split())

d = [sys.maxsize for _ in range(N)]
d[start - 1] = 0
heapq.heappush(h, (0, start - 1))

while h:
    tmpw, tmpv = heapq.heappop(h)
    if d[tmpv] < tmpw:
        continue
    for nv, nw in g[tmpv]:
        nextw = tmpw + nw
        if nextw < d[nv]:
            d[nv] = nextw
            heapq.heappush(h, (nextw, nv))

print(d[end - 1])

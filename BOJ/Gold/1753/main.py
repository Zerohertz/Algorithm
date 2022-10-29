import sys
import heapq
read = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, read().split())
K = int(read())

h = []
g = [[] for _ in range(V)]

for _ in range(E):
  u, v, w = map(int, read().split())
  g[u - 1].append((v - 1, w))

d = [INF for _ in range(V)]
d[K - 1] = 0
heapq.heappush(h, (0, K - 1))

while h:
  tmpw, tmpv = heapq.heappop(h)
  if d[tmpv] < tmpw:
    continue
  for nv, nw in g[tmpv]:
    nextw = tmpw + nw
    if nextw < d[nv]:
      d[nv] = nextw
      heapq.heappush(h, (nextw, nv))

for i in d:
  if i == INF:
    print('INF')
  else:
    print(i)
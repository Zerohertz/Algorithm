import sys
import heapq
read = sys.stdin.readline

N, M, X = map(int, read().split())
l = [[] for _ in range(N)]

for _ in range(M):
  a, b, c = map(int, read().split())
  l[a - 1].append((b - 1, c))

def Dijkstra(G, S):
  res = [sys.maxsize for _ in range(N)]
  res[S] = 0
  q = []
  heapq.heappush(q, (0, S))
  while q:
    d, tmp = heapq.heappop(q)
    if res[tmp] < d:
      continue
    for i, j in G[tmp]:
      if d + j < res[i]:
        res[i] = d + j
        heapq.heappush(q, (d + j, i))
  return res

res = 0
g = Dijkstra(l, X - 1)
for i in range(N):
  b = Dijkstra(l, i)
  res = max(res, g[i] + b[X - 1])

print(res)
import sys
import heapq
read = sys.stdin.readline

N, K = map(int, read().split())

jewel = []
for _ in range(N):
  M, V = map(int, read().split())
  heapq.heappush(jewel, (M, V))
jewel.sort()

bag = [0 for _ in range(K)]
for i in range(K):
  bag[i] = int(read())
bag.sort()

res = 0
tmp = []
for i in bag:
  while jewel and i >= jewel[0][0]:
    heapq.heappush(tmp, -jewel[0][1])
    heapq.heappop(jewel)
  if tmp:
    res += heapq.heappop(tmp)

print(-res)
import sys
import heapq
read = sys.stdin.readline

N = int(read())
l = []

for _ in range(N):
  heapq.heappush(l, int(read()))

if len(l) == 1:
  print(0)
else:
  res = 0
  while len(l) > 1:
    tmp1 = heapq.heappop(l)
    tmp2 = heapq.heappop(l)
    res += tmp1 + tmp2
    heapq.heappush(l, tmp1 + tmp2)
  print(res)
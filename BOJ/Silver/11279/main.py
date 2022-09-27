import sys
import heapq

read = sys.stdin.readline

N = int(read())
h = []
for _ in range(N):
  tmp = int(read())
  if tmp == 0:
    try:
      p = heapq.heappop(h)
      print(-p)
    except:
      print(0)
  else:
    heapq.heappush(h, -tmp)
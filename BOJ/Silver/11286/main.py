import sys
import heapq
read = sys.stdin.readline

N = int(read())
l = []
for _ in range(N):
  tmp = int(read())
  if tmp == 0:
    try:
      print(heapq.heappop(l)[1])
    except:
      print(0)
  else:
    heapq.heappush(l, (abs(tmp), tmp))
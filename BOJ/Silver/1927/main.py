import sys
import heapq
read = sys.stdin.readline

N = int(read())
h = []

for i in range(N):
  tmp = int(read())
  if tmp == 0:
    try:
      print(heapq.heappop(h))
    except:
      print(0)
  else:
    heapq.heappush(h, tmp)
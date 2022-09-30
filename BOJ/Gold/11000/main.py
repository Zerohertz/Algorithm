import sys
import heapq
read = sys.stdin.readline

N = int(read())
ST = []

for i in range(N):
  ST.append(list(map(int, read().split())))

ST.sort(key = lambda x: (x[0], x[1]))
G = []
heapq.heappush(G, ST[0][1])

for i in range(1, N):
  if ST[i][0] < G[0]:
    heapq.heappush(G, ST[i][1])
  else:
    heapq.heappop(G)
    heapq.heappush(G, ST[i][1])

print(len(G))
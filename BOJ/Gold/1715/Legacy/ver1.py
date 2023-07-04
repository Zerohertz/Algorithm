import heapq
import sys

read = sys.stdin.readline

N = int(read())
l = []

for _ in range(N):
    heapq.heappush(l, int(read()))

res = 0

for i in range(N):
    if i > 1:
        res += res + heapq.heappop(l)
    else:
        res += heapq.heappop(l)

print(res)

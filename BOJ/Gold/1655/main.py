import heapq
import sys

read = sys.stdin.readline

N = int(read())

l = []
r = []

for i in range(N):
    tmp = int(read())
    if len(l) == len(r):
        heapq.heappush(l, (-tmp, tmp))
    else:
        heapq.heappush(r, (tmp, tmp))
    if r and l[0][1] > r[0][1]:
        min = heapq.heappop(r)[1]
        max = heapq.heappop(l)[1]
        heapq.heappush(l, (-min, min))
        heapq.heappush(r, (max, max))
    print(l[0][1])

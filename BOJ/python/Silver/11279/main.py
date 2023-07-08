import heapq
import sys

read = sys.stdin.readline

N = int(read())
h = []
for _ in range(N):
    tmp = int(read())
    if tmp == 0:
        try:
            p = heapq.heappop(h)
            print(-p)
        except BaseException:
            print(0)
    else:
        heapq.heappush(h, -tmp)

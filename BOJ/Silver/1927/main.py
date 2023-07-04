import heapq
import sys

read = sys.stdin.readline

N = int(read())
h = []

for i in range(N):
    tmp = int(read())
    if tmp == 0:
        try:
            print(heapq.heappop(h))
        except BaseException:
            print(0)
    else:
        heapq.heappush(h, tmp)

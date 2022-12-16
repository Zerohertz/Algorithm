import sys
import heapq
read = sys.stdin.readline

N = int(read())
LPG = []
for i in range(N):
    a, b = map(int, read().split())
    heapq.heappush(LPG, (a, b))

L, P = map(int, read().split())

res = 0
sLPG = []
while P < L:
    while LPG and LPG[0][0] <= P:
        a, b = heapq.heappop(LPG)
        heapq.heappush(sLPG, (-b, a))
    if not sLPG:
        res = -1
        break
    P -= heapq.heappop(sLPG)[0]
    res += 1

print(res)
import heapq
import sys

read = sys.stdin.readline

T = int(read())
for _ in range(T):
    k = int(read())
    Mheap, mheap = [], []
    visit = [False] * 1_000_000
    for key in range(k):
        a, b = read().split()
        b = int(b)
        if a == "I":
            heapq.heappush(mheap, (b, key))
            heapq.heappush(Mheap, (-b, key))
            visit[key] = True
        elif a == "D":
            if b == -1:
                while mheap and not visit[mheap[0][1]]:
                    heapq.heappop(mheap)
                if mheap:
                    visit[mheap[0][1]] = False
                    heapq.heappop(mheap)
            elif b == 1:
                while Mheap and not visit[Mheap[0][1]]:
                    heapq.heappop(Mheap)
                if Mheap:
                    visit[Mheap[0][1]] = False
                    heapq.heappop(Mheap)
    while mheap and not visit[mheap[0][1]]:
        heapq.heappop(mheap)
    while Mheap and not visit[Mheap[0][1]]:
        heapq.heappop(Mheap)
    if mheap and Mheap:
        print(-Mheap[0][0], mheap[0][0])
    else:
        print("EMPTY")

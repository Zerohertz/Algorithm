import heapq
import sys

read = sys.stdin.readline

V, E = map(int, read().split())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, read().split())
    G[b].append([c, a])
    G[a].append([c, b])

l = [[0, 1]]
visit = [False for _ in range(V + 1)]
cnt = 0
cost = 0

while l:
    if cnt == V:
        break
    c, a = heapq.heappop(l)
    if not visit[a]:
        visit[a] = True
        cost += c
        cnt += 1
        for i in G[a]:
            heapq.heappush(l, i)

print(cost)

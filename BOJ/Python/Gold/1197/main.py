import heapq
import sys

read = sys.stdin.readline

if __name__ == "__main__":
    V, E = map(int, read().split())
    maps = [[] for _ in range(V)]
    for _ in range(E):
        A, B, C = map(int, read().split())
        maps[A - 1].append((B - 1, C))
        maps[B - 1].append((A - 1, C))
    cnt = 1
    results = 0
    visited = [False for _ in range(V)]
    paths = [(0, 0)]
    while paths and cnt <= V:
        weights, from_ = heapq.heappop(paths)
        if visited[from_]:
            continue
        visited[from_] = True
        cnt += 1
        results += weights
        for to_, weights in maps[from_]:
            if not visited[to_]:
                heapq.heappush(paths, (weights, to_))
    print(results)

"""
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
"""

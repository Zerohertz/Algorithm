import heapq
import sys

read = sys.stdin.readline

INF = sys.maxsize


def main():
    weights = [INF for _ in range(V)]
    weights[K - 1] = 0
    queue = [(0, K - 1)]
    while queue:
        w, v = heapq.heappop(queue)
        if weights[v] < w:
            continue
        for _w, _v in graph[v]:
            if weights[_v] <= w + _w:
                continue
            weights[_v] = w + _w
            heapq.heappush(queue, (w + _w, _v))
    for weight in weights:
        if weight == INF:
            print("INF")
            continue
        print(weight)


if __name__ == "__main__":
    V, E = map(int, read().split())
    K = int(read())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, read().split())
        graph[u - 1].append((w, v - 1))
    main()

"""1st
import heapq
import sys

read = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, read().split())
K = int(read())

h = []
g = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, read().split())
    g[u - 1].append((v - 1, w))

d = [INF for _ in range(V)]
d[K - 1] = 0
heapq.heappush(h, (0, K - 1))

while h:
    tmpw, tmpv = heapq.heappop(h)
    if d[tmpv] < tmpw:
        continue
    for nv, nw in g[tmpv]:
        nextw = tmpw + nw
        if nextw < d[nv]:
            d[nv] = nextw
            heapq.heappush(h, (nextw, nv))

for i in d:
    if i == INF:
        print("INF")
    else:
        print(i)
"""

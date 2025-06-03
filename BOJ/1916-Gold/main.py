import heapq
import sys

read = sys.stdin.readline

INF = sys.maxsize


def main():
    weights = [INF for _ in range(N)]
    weights[start - 1] = 0
    queue = [(0, start - 1)]
    while queue:
        w, v = heapq.heappop(queue)
        if weights[v] < w:
            continue
        for _w, _v in graph[v]:
            if weights[_v] <= w + _w:
                continue
            weights[_v] = w + _w
            heapq.heappush(queue, (w + _w, _v))
    print(weights[end - 1])


if __name__ == "__main__":
    N = int(read())
    M = int(read())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, read().split())
        graph[u - 1].append((w, v - 1))
    start, end = map(int, read().split())
    main()


"""1st
import heapq
import sys

read = sys.stdin.readline

N = int(read())
M = int(read())
h = []
g = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, read().split())
    g[a - 1].append((b - 1, c))

start, end = map(int, read().split())

d = [sys.maxsize for _ in range(N)]
d[start - 1] = 0
heapq.heappush(h, (0, start - 1))

while h:
    tmpw, tmpv = heapq.heappop(h)
    if d[tmpv] < tmpw:
        continue
    for nv, nw in g[tmpv]:
        nextw = tmpw + nw
        if nextw < d[nv]:
            d[nv] = nextw
            heapq.heappush(h, (nextw, nv))

print(d[end - 1])
"""

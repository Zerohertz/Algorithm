import heapq
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
parent = [i for i in range(N + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    univ = list(map(str, read().split()))
    path_sum = path_num = 0
    Map = []
    for _ in range(M):
        u, v, d = map(int, read().split())
        heapq.heappush(Map, (d, u, v))
    while Map:
        d, u, v = heapq.heappop(Map)
        if find_parent(u) != find_parent(v) and univ[u - 1] != univ[v - 1]:
            union_parent(u, v)
            path_sum += d
            path_num += 1
    if path_num == N - 1:
        print(path_sum)
    else:
        print(-1)

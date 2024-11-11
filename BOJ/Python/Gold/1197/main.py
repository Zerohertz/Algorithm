import heapq
import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**9)


class DistjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            self.parent[root2] = root1


if __name__ == "__main__":
    V, E = map(int, read().split())
    maps = []
    for _ in range(E):
        A, B, C = map(int, read().split())
        heapq.heappush(maps, (C, A - 1, B - 1))
    results = 0
    distjointset = DistjointSet(V)
    while maps:
        cost, node1, node2 = heapq.heappop(maps)
        if distjointset.find(node1) != distjointset.find(node2):
            distjointset.union(node1, node2)
            results += cost
    print(results)


"""2nd (Kruskal)
import heapq
import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**9)

class DistjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            self.parent[root2] = root1


if __name__ == "__main__":
    V, E = map(int, read().split())
    maps = []
    for _ in range(E):
        A, B, C = map(int, read().split())
        heapq.heappush(maps, (C, A - 1, B - 1))
    results = 0
    distjointset = DistjointSet(V)
    while maps:
        cost, node1, node2 = heapq.heappop(maps)
        if distjointset.find(node1) != distjointset.find(node2):
            distjointset.union(node1, node2)
            results += cost
    print(results)
"""

"""1st (Prim)
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

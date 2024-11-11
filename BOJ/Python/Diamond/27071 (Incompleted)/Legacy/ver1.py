import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**9)

MODULO = 998_244_353


class DistjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def main():
    edges.sort(key=lambda x: x[0])
    distjointset = DistjointSet(N)
    cnt = 1
    i = 0
    while i < M:
        weight = edges[i][0]
        same_weight_edges = []
        while i < M and edges[i][0] == weight:
            same_weight_edges.append(edges[i])
            i += 1
        valid_edges = []
        for _, node1, node2 in same_weight_edges:
            if distjointset.find(node1) == distjointset.find(node2):
                continue
            valid_edges.append((node1, node2))
        len_valid_edges = len(valid_edges)
        if 1 < len_valid_edges:
            _cnt = 1
            for j in range(2, len_valid_edges + 1):
                _cnt = (_cnt * j) % MODULO
            cnt = (cnt * _cnt) % MODULO
        for node1, node2 in valid_edges:
            distjointset.union(node1, node2)
    print(cnt % MODULO)


if __name__ == "__main__":
    N, M = map(int, read().split())
    edges = []
    for _ in range(M):
        A, B, C = map(int, read().split())
        edges.append((C, A - 1, B - 1))
    main()

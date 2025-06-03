import math
import sys

sys.setrecursionlimit(10**9)
read = sys.stdin.readline


class SegmentTree:
    def __init__(self, values):
        self.values = values
        self.length = len(values)
        size = math.ceil(math.log(self.length, 2) + 1e-9)
        size = 1 << (size + 1)
        self.tree = [0 for _ in range(size)]
        self._init()

    def _init(self, node=None, start=None, end=None):
        if node is None and start is None and end is None:
            node = 1
            start = 0
            end = self.length - 1
        if start == end:
            self.tree[node] = self.values[start]
            return self.tree[node]
        self.tree[node] = min(
            self._init(node * 2, start, (start + end) // 2),
            self._init(node * 2 + 1, (start + end) // 2 + 1, end),
        )
        return self.tree[node]

    def min(self, left, right, node=None, start=None, end=None):
        if node is None and start is None and end is None:
            node = 1
            start = 0
            end = self.length - 1
        if left > end or right < start:
            return sys.maxsize
        if left <= start and end <= right:
            return self.tree[node]
        return min(
            self.min(left, right, node * 2, start, (start + end) // 2),
            self.min(left, right, node * 2 + 1, (start + end) // 2 + 1, end),
        )


if __name__ == "__main__":
    N, M = map(int, read().split())
    l = [0 for _ in range(N)]
    for i in range(N):
        l[i] = int(read())
    st = SegmentTree(l)
    for _ in range(M):
        a, b = map(int, read().split())
        print(st.min(a - 1, b - 1))

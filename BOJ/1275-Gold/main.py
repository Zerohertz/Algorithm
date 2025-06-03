import math
import sys

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
        self.tree[node] = self._init(node * 2, start, (start + end) // 2) + self._init(
            node * 2 + 1, (start + end) // 2 + 1, end
        )
        return self.tree[node]

    def update(self, idx, value, node=None, start=None, end=None):
        if node is None and start is None and end is None:
            diff = value - self.values[idx]
            self.values[idx] = value
            value = diff
            node = 1
            start = 0
            end = self.length - 1
        if idx < start or idx > end:
            return None
        self.tree[node] += value
        if start != end:
            self.update(idx, value, node * 2, start, (start + end) // 2)
            self.update(idx, value, node * 2 + 1, (start + end) // 2 + 1, end)

    def sum(self, left, right, node=None, start=None, end=None):
        if node is None and start is None and end is None:
            node = 1
            start = 0
            end = self.length - 1
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        return self.sum(left, right, node * 2, start, (start + end) // 2) + self.sum(
            left, right, node * 2 + 1, (start + end) // 2 + 1, end
        )


if __name__ == "__main__":
    N, Q = map(int, read().split())
    l = list(map(int, read().split()))
    st = SegmentTree(l)
    for _ in range(Q):
        x, y, a, b = map(int, read().split())
        x, y = min(x, y), max(x, y)
        print(st.sum(x - 1, y - 1))
        st.update(a - 1, b)

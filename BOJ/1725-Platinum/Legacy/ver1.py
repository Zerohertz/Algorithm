import math
import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**9)


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
            self.tree[node] = start
            return self.tree[node]
        idx1 = self._init(node * 2, start, (start + end) // 2)
        idx2 = self._init(node * 2 + 1, (start + end) // 2 + 1, end)
        if self.values[idx1] <= self.values[idx2]:
            self.tree[node] = idx1
        else:
            self.tree[node] = idx2
        return self.tree[node]

    def __call__(self, left, right, node=None, start=None, end=None):
        if node is None and start is None and end is None:
            node = 1
            start = 0
            end = self.length - 1
        if left > end or right < start:
            return -1
        if left <= start and end <= right:
            return self.tree[node]
        idx1 = self(left, right, 2 * node, start, (start + end) // 2)
        idx2 = self(left, right, 2 * node + 1, (start + end) // 2 + 1, end)
        if idx1 == -1:
            return idx2
        elif idx2 == -1:
            return idx1
        if self.values[idx1] <= self.values[idx2]:
            return idx1
        return idx2

    def large(self, start=None, end=None):
        if start is None and end is None:
            start = 0
            end = self.length - 1
        if start == end:
            return self.values[start]
        idx = self(start, end)
        area = (end - start + 1) * self.values[idx]
        if start <= idx - 1:
            tmp = self.large(start, idx - 1)
            area = max(area, tmp)
        if idx + 1 <= end:
            tmp = self.large(idx + 1, end)
            area = max(area, tmp)
        return area


if __name__ == "__main__":
    N = int(read())
    L = [0 for _ in range(N)]
    for i in range(N):
        L[i] = int(read())
    st = SegmentTree(L)
    print(st.large())

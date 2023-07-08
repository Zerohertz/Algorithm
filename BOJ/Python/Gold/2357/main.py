import sys

sys.setrecursionlimit(10**9)
read = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = (l[start], l[start])
        return tree[node]
    else:
        x = init(node * 2, start, (start + end) // 2)
        y = init(node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = (min(x[0], y[0]), max(x[1], y[1]))
        return tree[node]


def segMinMax(node, start, end, left, right):
    if left > end or right < start:
        return (sys.maxsize, -sys.maxsize)
    if left <= start and end <= right:
        return tree[node]
    x = segMinMax(node * 2, start, (start + end) // 2, left, right)
    y = segMinMax(node * 2 + 1, (start + end) // 2 + 1, end, left, right)
    return (min(x[0], y[0]), max(x[1], y[1]))


N, M = map(int, read().split())

l = [0 for _ in range(N)]
for i in range(N):
    l[i] = int(read())

tree = [(sys.maxsize, -sys.maxsize) for _ in range(400_000)]
init(1, 0, N - 1)

for _ in range(M):
    a, b = map(int, read().split())
    a, b = segMinMax(1, 0, N - 1, a - 1, b - 1)
    print(a, b)

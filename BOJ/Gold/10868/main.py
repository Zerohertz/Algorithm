import sys

sys.setrecursionlimit(10 ** 9)
read = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        x = init(node * 2, start, (start + end) // 2)
        y = init(node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = min(x, y)
        return tree[node]


def segMin(node, start, end, left, right):
    if left > end or right < start:
        return sys.maxsize
    if left <= start and end <= right:
        return tree[node]
    x = segMin(node * 2, start, (start + end) // 2, left, right)
    y = segMin(node * 2 + 1, (start + end) // 2 + 1, end, left, right)
    return min(x, y)


N, M = map(int, read().split())

l = [0 for _ in range(N)]
for i in range(N):
    l[i] = int(read())

tree = [(sys.maxsize, -sys.maxsize) for _ in range(400_000)]
init(1, 0, N - 1)

for _ in range(M):
    a, b = map(int, read().split())
    print(segMin(1, 0, N - 1, a - 1, b - 1))

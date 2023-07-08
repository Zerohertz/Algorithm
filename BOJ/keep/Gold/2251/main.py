import sys
from collections import deque


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))


read = sys.stdin.readline
A, B, C = map(int, read().split())
visited = [[False for _ in range(B + 1)] for _ in range(A + 1)]
q = deque()
q.append((0, 0))
visited[0][0] = True
res = []
while q:
    x, y = q.popleft()
    z = C - x - y
    if x == 0:
        res.append(z)
    tmp = min(x, B - y)
    pour(x - tmp, y + tmp)
    tmp = min(x, C - z)
    pour(x - tmp, y)
    tmp = min(y, A - x)
    pour(x + tmp, y - tmp)
    tmp = min(y, C - z)
    pour(x, y - tmp)
    tmp = min(z, A - x)
    pour(x + tmp, y)
    tmp = min(z, B - y)
    pour(x, y + tmp)

res.sort()
for i in res:
    print(i, end=" ")

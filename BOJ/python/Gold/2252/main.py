import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())
l = [0 for _ in range(N + 1)]
g = [deque() for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, read().split())
    l[b] += 1
    g[a].append(b)

q = deque()
for i in range(1, N + 1):
    if l[i] == 0:
        q.append(i)

res = []
while q:
    tmp = q.popleft()
    res.append(tmp)
    for i in g[tmp]:
        l[i] -= 1
        if l[i] == 0:
            q.append(i)

print(*res)

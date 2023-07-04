import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())
g = [[] for _ in range(N + 1)]
rank = [0 for _ in range(N + 1)]

for _ in range(M):
    tmp = list(map(int, read().split()))
    for i in range(1, tmp[0]):
        g[tmp[i]].append(tmp[i + 1])
        rank[tmp[i + 1]] += 1

q = deque()
for i in range(1, N + 1):
    if rank[i] == 0:
        q.append(i)

res = []
while q:
    tmp = q.popleft()
    res.append(tmp)
    for i in g[tmp]:
        rank[i] -= 1
        if rank[i] == 0:
            q.append(i)

if len(res) != N:
    print(0)
else:
    for i in res:
        print(i)

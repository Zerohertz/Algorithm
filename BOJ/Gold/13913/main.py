import sys
from collections import deque

read = sys.stdin.readline


def BFS(N, K):
    q = deque()
    q.append(N)
    while q:
        tmp = q.popleft()
        if tmp == K:
            print(l[tmp])
            break
        for x in (tmp - 1, tmp + 1, tmp * 2):
            if 0 <= x <= 100_000 and not l[x]:
                l[x] = l[tmp] + 1
                q.append(x)
                c[x] = tmp


N, K = map(int, read().split())
l = [0 for i in range(100_001)]
c = [0 for i in range(100_001)]
BFS(N, K)
res = []
tmp = K
for _ in range(l[K] + 1):
    res.append(tmp)
    tmp = c[tmp]
for i in res[::-1]:
    print(i, end=' ')

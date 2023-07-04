import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
l = [[0 for _ in range(N)] for _ in range(N)]

m = sys.maxsize
M = 0
for i in range(N):
    l[i] = list(map(int, read().split()))
    m = min(m, min(l[i]))
    M = max(M, max(l[i]))

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]


def BFS(s1, s2, k):
    q = deque([(s1, s2)])
    v[s1][s2] = True
    while q:
        tmp = q.popleft()
        for i, j in zip(v1, v2):
            if 0 <= tmp[0] + i < N and 0 <= tmp[1] + j < N:
                if l[tmp[0] + i][tmp[1] + j] > k and not v[tmp[0] + i][tmp[1] + j]:
                    q.append((tmp[0] + i, tmp[1] + j))
                    v[tmp[0] + i][tmp[1] + j] = True


res = 1
for k in range(m, M):
    v = [[False for _ in range(N)] for _ in range(N)]
    tmpres = 0
    for i in range(N):
        for j in range(N):
            if l[i][j] > k and not v[i][j]:
                BFS(i, j, k)
                tmpres += 1
    res = max(res, tmpres)
print(res)

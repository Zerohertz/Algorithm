import sys
from collections import deque
from itertools import combinations

read = sys.stdin.readline

N, M = map(int, read().split())
l = [[0 for _ in range(M)] for _ in range(N)]

wallcandidate = []
nW = 0
viruspos = []
for i in range(N):
    l[i] = list(map(int, read().split()))
    for j in range(M):
        if l[i][j] == 0:
            wallcandidate.append((i, j))
        elif l[i][j] == 1:
            nW += 1
        elif l[i][j] == 2:
            viruspos.append((i, j))

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]


def BFS(newwall):
    q = deque()
    for i in viruspos:
        q.append(i)
    cnt = 0
    v[q[0][0]][q[0][1]] = True
    while q:
        x, y = q.popleft()
        cnt += 1
        for i, j in zip(v1, v2):
            nx = x + i
            ny = y + j
            if 0 <= nx < N and 0 <= ny < M:
                if (nx, ny) in newwall:
                    continue
                if l[nx][ny] == 0 and not v[nx][ny]:
                    v[nx][ny] = True
                    q.append((nx, ny))
                # elif l[nx][ny] == 2 and not v[nx][ny]:
                #   v[nx][ny] = True
                #   q.append((nx, ny))
    return cnt


res = 0
for wc in combinations(wallcandidate, 3):
    v = [[False for _ in range(M)] for _ in range(N)]
    res = max(res, N * M - nW - 3 - BFS(wc))

print(res)

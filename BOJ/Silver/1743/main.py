import sys
from collections import deque

read = sys.stdin.readline

N, M, K = map(int, read().split())
G = [[0 for _ in range(M)] for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

for _ in range(K):
    a, b = map(int, read().split())
    G[a - 1][b - 1] = 1

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]


def BFS(x, y):
    q = deque([(x, y)])
    size = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + v1[i]
            ny = y + v2[i]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and G[nx][ny] == 1:
                visit[nx][ny] = True
                size += 1
                q.append((nx, ny))
    return size


res = 0
for i in range(N):
    for j in range(M):
        if not visit[i][j] and G[i][j] == 1:
            visit[i][j] = True
            res = max(res, BFS(i, j))

print(res)

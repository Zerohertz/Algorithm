import sys
from collections import deque

read = sys.stdin.readline

N, M, A, B, K = map(int, read().split())

G = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    a, b = map(int, read().split())
    G[a - 1][b - 1] = -1

x, y = map(int, read().split())
x -= 1
y -= 1
ex, ey = map(int, read().split())
ex -= 1
ey -= 1

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]

q = deque([(x, y, 0)])
while q:
    x, y, cnt = q.popleft()
    if x == ex and y == ey:
        print(cnt)
        exit()
    for i in range(4):
        status = True
        nx, ny = x + v1[i], y + v2[i]
        if 0 <= nx <= N - A and 0 <= ny <= M - B:
            if G[nx][ny] == 0:
                for j in range(A):
                    for k in range(B):
                        if G[nx + j][ny + k] == -1:
                            status = False
                if status:
                    G[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))

print(-1)

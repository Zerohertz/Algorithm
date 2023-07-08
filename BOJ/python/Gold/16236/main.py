import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
G = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    G[i] = list(map(int, read().split()))
    for j in range(N):
        if G[i][j] == 9:
            BabyShark = [i, j, 2, 0, 0]

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]


def BFS(x, y, lv):
    q = deque([(x, y)])
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    visit[x][y] = 0
    while q:
        x, y = q.popleft()
        for d1, d2 in zip(v1, v2):
            nx = x + d1
            ny = y + d2
            if 0 <= nx < N and 0 <= ny < N:
                if 0 <= G[nx][ny] <= lv and visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
    return visit


def distance(visit, lv):
    x, y = 0, 0
    dt = sys.maxsize
    for i in range(N):
        for j in range(N):
            if visit[i][j] != -1 and 1 <= G[i][j] < lv:
                if visit[i][j] < dt:
                    dt = visit[i][j]
                    x, y = i, j
    if dt == sys.maxsize:
        return False
    else:
        return (x, y, dt)


G[BabyShark[0]][BabyShark[1]] = 0
while True:
    x, y, lv, cnt, t = BabyShark
    res = distance(BFS(x, y, lv), lv)
    if not res:
        print(t)
        break
    else:
        G[res[0]][res[1]] = 0
        if cnt + 1 == lv:
            BabyShark = [res[0], res[1], lv + 1, 0, t + res[2]]
        else:
            BabyShark = [res[0], res[1], lv, cnt + 1, t + res[2]]

import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
l = [["" for _ in range(N)] for _ in range(N)]
juklock = [["" for _ in range(N)] for _ in range(N)]
for i in range(N):
    l[i] = list(read().rstrip())
    for j in range(N):
        if l[i][j] == "G":
            juklock[i][j] = "R"
        else:
            juklock[i][j] = l[i][j]

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]


def BFS(l, initPos):
    q = deque([initPos])
    visit[initPos[0]][initPos[1]] = True
    color = l[initPos[0]][initPos[1]]
    while q:
        x, y = q.popleft()
        for i, j in zip(v1, v2):
            nx = x + i
            ny = y + j
            if 0 <= nx < N and 0 <= ny < N:
                if l[nx][ny] == color and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))


visit = [[False for _ in range(N)] for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            BFS(l, (i, j))
            cnt1 += 1

visit = [[False for _ in range(N)] for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            BFS(juklock, (i, j))
            cnt2 += 1

print(cnt1, cnt2)

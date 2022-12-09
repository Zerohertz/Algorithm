import sys
from collections import deque

read = sys.stdin.readline

R, C = map(int, read().split())
G = [['' for _ in range(C)] for _ in range(R)]
time = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    G[i] = list(read().rstrip())
    for j in range(C):
        if G[i][j] == 'D':
            D = (i, j)
        elif G[i][j] == 'S':
            S = (i, j)

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]

def BFS():
    while q:
        x, y = q.popleft()
        if G[D[0]][D[1]] == 'S':
            return time[D[0]][D[1]]
        for i in range(4):
            nx, ny = x + v1[i], y + v2[i]
            if 0 <= nx < R and 0 <= ny < C:
                if (G[nx][ny] == '.' or G[nx][ny] == 'S') and G[x][y] == '*':
                    G[nx][ny] = '*'
                    q.append((nx, ny))
                elif (G[nx][ny] == '.' or G[nx][ny] == 'D') and G[x][y] == 'S':
                    G[nx][ny] = 'S'
                    time[nx][ny] = time[x][y] + 1
                    q.append((nx, ny))
    return "KAKTUS"

q = deque([S])
for i in range(R):
    for j in range(C):
        if G[i][j] == '*':
            q.append((i, j))

print(BFS())
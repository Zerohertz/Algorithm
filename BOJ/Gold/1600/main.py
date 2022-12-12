import sys
from collections import deque
read = sys.stdin.readline

K = int(read())
W, H = map(int, read().split())

G = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
  G[i] = list(map(int, read().split()))

m1 = [1, 0, -1, 0]
m2 = [0, 1, 0, -1]

h1 = [2, 1, -1, -2, -2, -1, 1, 2]
h2 = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS():
  q = deque([(0, 0, K)])
  visited = [[[0 for _ in range(31)] for _ in range(W)] for _ in range(H)]
  while q:
    x, y, tmpK = q.popleft()
    if x == H - 1 and y == W - 1:
      return visited[x][y][tmpK]
    for i in range(4):
      nx, ny = x + m1[i], y + m2[i]
      if 0 <= nx < H and 0 <= ny < W and not G[nx][ny] == 1 and visited[nx][ny][tmpK] == 0:
        visited[nx][ny][tmpK] = visited[x][y][tmpK] + 1
        q.append((nx, ny, tmpK))
    if tmpK > 0:
      for i in range(8):
        nx, ny = x + h1[i], y + h2[i]
        if 0 <= nx < H and 0 <= ny < W and not G[nx][ny] == 1 and visited[nx][ny][tmpK - 1] == 0:
          visited[nx][ny][tmpK - 1] = visited[x][y][tmpK] + 1
          q.append((nx, ny, tmpK - 1))
  return -1

print(BFS())
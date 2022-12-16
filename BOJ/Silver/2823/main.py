import sys
from collections import deque
read = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def bfs(v):
  q = deque([v])
  while q:
    x, y = q.popleft()
    cnt = 0
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < r and 0 <= ny < c and G[nx][ny] == ".":
        cnt += 1
        if not visited[nx][ny]:
          visited[nx][ny] = True
          q.append([nx, ny])
    if cnt < 2:
      return 1
  return 0

r, c = map(int, read().split())
l = []
G = []
for i in range(r):
  G.append(list(map(str, read().strip())))
  for j in range(c):
    if G[i][j] == ".":
      l.append([i, j])

visited = [[False for _ in range(c)] for _ in range(r)]
print(bfs(l[0]))
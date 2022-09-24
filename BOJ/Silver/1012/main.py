import sys
from collections import deque
read = sys.stdin.readline

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]

def bfs(g, i, j):
  queue = deque()
  queue.append((i, j))
  g[i][j] = 0
  while queue:
    x, y = queue.popleft()
    for k in range(4):
      tmpx = x + v1[k]
      tmpy = y + v2[k]
      if 0 > tmpx or 0 > tmpy or tmpx >= M or tmpy >= N:
        continue
      if g[tmpx][tmpy] == 1:
        g[tmpx][tmpy] = 0
        queue.append((tmpx, tmpy))
  return

T = int(read())
for _ in range(T):
  M, N, K = map(int, read().split())
  g = [[0 for i in range(N)] for i in range(M)]
  for _ in range(K):
    x, y = map(int, read().split())
    g[x][y] = 1
  cnt = 0
  for i in range(M):
    for j in range(N):
      if g[i][j] == 1:
        bfs(g, i, j)
        cnt += 1
  print(cnt)
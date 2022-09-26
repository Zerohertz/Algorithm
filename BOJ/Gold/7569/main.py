import sys
from collections import deque
read = sys.stdin.readline

def bfs(g):
  v1 = [0, 0, 0, 0, -1, 1]
  v2 = [1, 0, -1, 0, 0, 0]
  v3 = [0, 1, 0, -1, 0, 0]
  while q:
    z1, y1, x1 = q.popleft()
    for i in range(6):
      z2 = z1 + v1[i]
      y2 = y1 + v2[i]
      x2 = x1 + v3[i]
      if 0 <= x2 and x2 < M and 0 <= y2 and y2 < N and 0 <= z2 and z2 < H and g[z2][y2][x2] == 0:
        q.append([z2, y2, x2])
        g[z2][y2][x2] = g[z1][y1][x1] + 1

M, N, H = map(int, read().split())
l = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
q = deque()

for i in range(H):
  for j in range(N):
    l[i][j] = list(map(int, read().split()))
    for k in range(M):
      if l[i][j][k] == 1:
        q.append([i, j, k])

bfs(l)
res = 0
for i in l:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        exit(0)
    res = max(res, max(j))

print(res - 1)
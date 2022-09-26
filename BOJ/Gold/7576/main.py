import sys
from collections import deque
read = sys.stdin.readline

def bfs(g):
  v1 = [1, 0, -1, 0]
  v2 = [0, 1, 0, -1]
  while q:
    x1, y1 = q.popleft()
    for i in range(4):
      x2 = x1 + v1[i]
      y2 = y1 + v2[i]
      if 0 <= x2 and x2 < N and 0 <= y2 and y2 < M and g[x2][y2] == 0:
        q.append([x2, y2])
        g[x2][y2] = g[x1][y1] + 1

M, N = map(int, read().split())
l = [[0 for _ in range(M)] for _ in range(N)]
q = deque()

for i in range(N):
  l[i] = list(map(int, read().split()))
  for j in range(M):
    if l[i][j] == 1:
      q.append([i, j])

bfs(l)
res = 0
for i in l:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  res = max(res, max(i))

print(res - 1)
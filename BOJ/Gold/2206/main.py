import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
l = [[0 for _ in range(M)] for _ in range(N)]
v = [[[0, 0] for _ in range(M)] for _ in range(N)]

for i in range(N):
  l[i] = list(map(int, read().rstrip()))

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]

q = deque([(0, 0, 0)])
v[0][0][0] = 1

while q:
  x, y, b = q.popleft()
  if x == N - 1 and y == M - 1:
    print(v[x][y][b])
    exit(0)
  for i, j in zip(v1, v2):
    if x + i >= 0 and x + i < N and y + j >= 0 and y + j < M:
      if l[x + i][y + j] == 1 and b == 0:
        v[x + i][y + j][1] = v[x][y][0] + 1
        q.append((x + i, y + j, 1))
      elif l[x + i][y + j] == 0 and v[x + i][y + j][b] == 0:
        v[x + i][y + j][b] = v[x][y][b] + 1
        q.append((x + i, y + j, b))
print(-1)
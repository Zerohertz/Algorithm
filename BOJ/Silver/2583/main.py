import sys
from collections import deque
read = sys.stdin.readline

M, N, K = map(int, read().split())

l = [[0 for _ in range(M)] for _ in range(N)]

def draw(x1, y1, x2, y2):
  for i in range(x1, x2):
    for j in range(y1, y2):
      l[i][j] += 1

for k in range(K):
  a, b, c, d = map(int, read().split())
  draw(a, b, c, d)

cnt = 0
res = []
visit = [[False for _ in range(M)] for _ in range(N)]
q = deque()
v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]
for i in range(N):
  for j in range(M):
    if not visit[i][j] and l[i][j] == 0:
      sz = 0
      q.append((i, j))
      while q:
        x, y = q.popleft()
        for ii, jj in zip(v1, v2):
          nx, ny = x + ii, y + jj
          if 0 <= nx < N and 0 <= ny < M:
            if not visit[nx][ny] and l[nx][ny] == 0:
              visit[nx][ny] = True
              q.append((nx, ny))
              sz += 1
      cnt += 1
      res.append(sz)

res.sort()
print(cnt)
for i in res:
  if i == 0:
    print(1, end = ' ')
  else:
    print(i, end = ' ')
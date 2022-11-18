import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())

l = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
  l[i] = list(map(int, read().split()))

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]
def BFS(x, y):
  res = 1
  q = deque([(x, y)])
  visit[x][y] = True
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + v1[i], y + v2[i]
      if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and l[nx][ny] == 1:
        visit[nx][ny] = True
        q.append((nx, ny))
        res += 1
  return res

visit = [[False for _ in range(m)] for _ in range(n)]

cnt = 0
size = 0
for i in range(n):
  for j in range(m):
    if not visit[i][j] and l[i][j] == 1:
      size = max(size, BFS(i, j))
      cnt += 1

print(cnt)
print(size)
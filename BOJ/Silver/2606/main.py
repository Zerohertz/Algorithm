import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
M = int(read())

l = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
  a, b = map(int, read().split())
  l[a - 1][b - 1] = 1
  l[b - 1][a - 1] = 1

g = [0 for _ in range(N)]
q = deque()
q.append(0)
while q:
  tmp = q.popleft()
  g[tmp] = 1
  for i in range(N):
    if l[tmp][i] == 1:
      q.append(i)
      l[tmp][i] = 0
      g[i] = 1

cnt = -1
for i in g:
  if i == 1:
    cnt += 1
print(cnt)
import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
l = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, read().split())
  l[a - 1].append(b - 1)
  l[b - 1].append(a - 1)

g = [False for _ in range(N)]
q = deque()

cnt = 0
for j in range(N):
  if not g[j]:
    if not l[j]:
      g[j] = True
      cnt += 1
    else:
      q.append(j)
      g[j] = True
      while q:
        tmp = q.popleft()
        for i in l[tmp]:
          if not g[i]:
            q.append(i)
            g[i] = True
      cnt += 1

print(cnt)
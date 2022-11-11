import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
l = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, read().split())
  l[a - 1].append(b - 1)
  l[b - 1].append(a - 1)

def BFS(start):
  q = deque([(start, 0)])
  visit = [False for _ in range(N)]
  KevinBacon = [0 for _ in range(N)]
  visit[start] = True
  while q:
    tmp = q.popleft()
    for i in l[tmp[0]]:
      if not visit[i]:
        visit[i] = True
        KevinBacon[i] = tmp[1] + 1
        q.append((i, tmp[1] + 1))
  return sum(KevinBacon)

res = []
for i in range(N):
  res.append(BFS(i))

print(res.index(min(res)) + 1)
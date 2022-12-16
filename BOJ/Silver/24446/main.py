import sys
from collections import deque
read = sys.stdin.readline

N, M, R = map(int, read().split())
G = [[] for _ in range(N)]
for _ in range(M):
  u, v = map(int, read().split())
  G[u - 1].append(v - 1)
  G[v - 1].append(u - 1)

q = deque([(R - 1, 0)])
visited = [-1 for _ in range(N)]
visited[R - 1] = 0
while q:
  tmp, depth = q.popleft()
  for i in G[tmp]:
    if visited[i] == -1:
      visited[i] = depth + 1
      q.append((i, depth + 1))

for i in visited:
  print(i)
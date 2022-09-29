import sys
from collections import deque
read = sys.stdin.readline

def DFS(initPos):
  print(initPos, end = ' ')
  v[initPos] = True
  for i in g[initPos]:
    if not v[i]:
      DFS(i)
      v[i] = True

def BFS(initPos):
  q.append(initPos)
  v[initPos] = True
  while q:
    tmp = q.popleft()
    print(tmp, end = ' ')
    for i in g[tmp]:
      if not v[i]:
        v[i] = True
        q.append(i)

N, M, V = map(int, read().split())
g = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, read().split())
  g[a].append(b)
  g[b].append(a)

for i in range(N + 1):
  g[i].sort()

v = [False for _ in range(N + 1)]
DFS(V)
print()

q = deque()
v = [False for _ in range(N + 1)]
BFS(V)
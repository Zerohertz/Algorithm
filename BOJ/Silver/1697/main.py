import sys
from collections import deque
read = sys.stdin.readline

def bfs(N, K):
  q = deque()
  q.append(N)
  while q:
    tmp = q.popleft()
    if tmp == K:
      print(l[tmp])
      break
    for x in (tmp - 1, tmp + 1, tmp * 2):
      if 0 <= x <= 100_000 and not l[x]:
        l[x] = l[tmp] + 1
        q.append(x)

N, K = map(int, read().split())
l = [0 for i in range(100_001)]
bfs(N, K)
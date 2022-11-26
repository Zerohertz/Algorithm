import sys
from collections import deque
read = sys.stdin.readline

T = int(read())
for _ in range(T):
  N, K = map(int, read().split())
  D = [0] + list(map(int, read().split()))
  G = [[] for _ in range(N + 1)]
  rank = [0 for _ in range(N + 1)]
  for _ in range(K):
    a, b = map(int, read().split())
    G[a].append(b)
    rank[b] += 1
  W = int(read())
  dp = [0 for _ in range(N + 1)]
  q = deque()
  for i in range(1, N + 1):
    if rank[i] == 0:
      q.append(i)
      dp[i] = D[i]
  while q:
    tmp = q.popleft()
    for i in G[tmp]:
      rank[i] -= 1
      dp[i] = max(dp[i], D[i] + dp[tmp])
      if rank[i] == 0:
        q.append(i)
  print(dp[W])
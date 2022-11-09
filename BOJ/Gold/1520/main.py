import sys
sys.setrecursionlimit(100_000)
read = sys.stdin.readline

M, N = map(int, read().split())
l = [[0 for _ in range(N)] for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

for i in range(M):
  l[i] = list(map(int, read().split()))

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]
res = [0]

def DFS(start):
  x, y = start
  if x == M - 1 and y == N - 1:
    return 1
  if dp[x][y] != -1:
    return dp[x][y]
  tmp = 0
  for i, j in zip(v1, v2):
    nx = x + i
    ny = y + j
    if 0 <= nx < M and 0 <= ny < N:
      if l[x][y] > l[nx][ny]:
        tmp += DFS((nx, ny))
  dp[x][y] = tmp
  return dp[x][y]

print(DFS((0, 0)))
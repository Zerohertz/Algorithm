import sys
read = sys.stdin.readline

N, M = map(int, read().split())
m = [0] + list(map(int, read().split()))
c = [0] + list(map(int, read().split()))
C = sum(c)
dp = [[0 for _ in range(C + 1)] for _ in range(N + 1)]

res = sys.maxsize
for i in range(N + 1):
  tmpm = m[i]
  tmpc = c[i]
  for j in range(C + 1):
    if j < tmpc:
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - tmpc] + tmpm)
    if dp[i][j] >= M:
      res = min(res, j)

if M == 0:
  print(0)
else:
  print(res)
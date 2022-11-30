import sys
read = sys.stdin.readline

N = int(read())
l = [list(map(int, read().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
  for j in range(N - i):
    x = i + j
    dp[j][x] = sys.maxsize
    for k in range(j, x):
      dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + l[j][0] * l[k][1] * l[x][1])

print(dp[0][N - 1])
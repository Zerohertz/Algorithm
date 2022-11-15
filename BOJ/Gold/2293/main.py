import sys
read = sys.stdin.readline

n, k = map(int, read().split())

coins = [0 for _ in range(n)]
dp = [0 for _ in range(k + 1)]
dp[0] = 1
for i in range(n):
  coins[i] = int(read())

for coin in coins:
  for j in range(coin, k + 1):
    if j - coin >= 0:
      dp[j] += dp[j - coin]
print(dp[k])
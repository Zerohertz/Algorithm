import sys

read = sys.stdin.readline

dp = [0 for _ in range(31)]
dp[2] = 3
dp[4] = 11

for i in range(6, 31, 2):
    dp[i] = 3 * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2

print(dp[int(read())])

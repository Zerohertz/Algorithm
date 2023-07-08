import sys

read = sys.stdin.readline

N = int(read())

l = [0 for _ in range(302)]
dp = [0 for _ in range(302)]

for i in range(1, N + 1):
    l[i] = int(read())

dp[1] = l[1]
dp[2] = l[1] + l[2]
dp[3] = max(l[1] + l[3], l[2] + l[3])

for i in range(4, N + 1):
    dp[i] = max(dp[i - 3] + l[i - 1] + l[i], dp[i - 2] + l[i])

print(dp[N])

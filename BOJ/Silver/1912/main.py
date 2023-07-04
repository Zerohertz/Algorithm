import sys

read = sys.stdin.readline

n = int(read())
l = list(map(int, read().split()))

dp = [l[0]]

for i in range(1, n):
    dp.append(max(l[i], dp[i - 1] + l[i]))

print(max(dp))

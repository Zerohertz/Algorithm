import sys

read = sys.stdin.readline

A = read().rstrip()
B = read().rstrip()

lA = len(A)
lB = len(B)

dp = [[0 for _ in range(lB + 1)] for _ in range(lA + 1)]

for i in range(lA):
    for j in range(lB):
        if A[i] == B[j]:
            dp[i + 1][j + 1] += dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

print(dp[-1][-1])

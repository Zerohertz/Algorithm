import sys

A = [0] + list(sys.stdin.readline().rstrip())
B = [0] + list(sys.stdin.readline().rstrip())

Na = len(A)
Nb = len(B)

dp = [["" for _ in range(Nb)] for _ in range(Na)]

for i in range(1, Na):
    for j in range(1, Nb):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + A[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[Na - 1][Nb - 1]))
print(dp[Na - 1][Nb - 1])

import sys

read = sys.stdin.readline

N = int(read())
L = [sys.maxsize] + list(map(int, read().split()))
M = int(read())

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for tmp in range(0, N):
    for idx1 in range(1, N + 1 - tmp):
        idx2 = idx1 + tmp
        if idx1 == idx2:
            dp[idx1][idx2] = 1
        elif L[idx1] == L[idx2]:
            if idx1 + 1 == idx2:
                dp[idx1][idx2] = 1
            elif dp[idx1 + 1][idx2 - 1] == 1:
                dp[idx1][idx2] = 1

for _ in range(M):
    S, E = map(int, read().split())
    print(dp[S][E])

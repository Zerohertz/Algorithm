import sys

sys.setrecursionlimit(10**9)
read = sys.stdin.readline

N = int(read())
l = [0 for _ in range(N)]
for i in range(N):
    l[i] = int(read())

dp = [[0 for _ in range(N)] for _ in range(N)]


def solution(idx1, idx2, cnt):
    if idx1 == idx2:
        return cnt * l[idx1]
    if dp[idx1][idx2]:
        return dp[idx1][idx2]
    dp[idx1][idx2] = max(
        solution(idx1 + 1, idx2, cnt + 1) + cnt * l[idx1],
        solution(idx1, idx2 - 1, cnt + 1) + cnt * l[idx2],
    )
    return dp[idx1][idx2]


print(solution(0, N - 1, 1))

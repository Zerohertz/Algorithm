import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, read().split())
    A = list(map(int, read().split()))
    P = 0
    dp = [0 for _ in range(M)]
    for a in A:
        P += a
        dp[P % M] += 1
    res = dp[0]
    for d in dp:
        res += (d * (d - 1)) / 2
    print(int(res))

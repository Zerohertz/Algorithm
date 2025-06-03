import sys

read = sys.stdin.readline
MOD = 1_000_000


def main():
    dp = [0 for _ in range(n + 1)]
    dp[0] = dp[1] = 1
    if code[0] == 0:
        return 0
    for i in range(1, n):
        if 0 < code[i]:
            dp[i + 1] += dp[i]
        if 10 <= code[i - 1] * 10 + code[i] <= 26:
            dp[i + 1] += dp[i - 1]
    return dp[n] % MOD


if __name__ == "__main__":
    code = list(map(int, list(read().rstrip())))
    n = len(code)
    print(main())

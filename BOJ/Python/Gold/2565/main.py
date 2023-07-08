import sys

if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    l = [[0, 0] for _ in range(N)]
    dp = [0 for _ in range(N)]
    for i in range(N):
        a, b = map(int, read().split())
        l[i] = [a, b]
    l.sort(key=lambda x: x[0])
    for i in range(N):
        for j in range(i):
            if l[i][1] > l[j][1] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    print(N - max(dp))

import sys

read = sys.stdin.readline

if __name__ == "__main__":
    T = int(read())
    for _ in range(T):
        K = int(read())
        L = list(map(int, read().split()))
        ss = {-1: 0}
        for i in range(K):
            ss[i] = ss[i - 1] + L[i]
        dp = [[0 for _ in range(K)] for _ in range(K)]
        for i in range(1, K):
            for j in range(K - 1):
                k = i + j
                if k >= K:
                    break
                res = sys.maxsize
                for z in range(j, k):
                    res = min(res, dp[j][z] + dp[z + 1][k] + ss[k] - ss[j - 1])
                dp[j][k] = res
        print(dp[0][-1])

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(node):
    global cnt
    visited[node] = True
    for node_ in sns[node]:
        if visited[node_]:
            continue
        dfs(node_)
        dp[node][1] += min(dp[node_][0], dp[node_][1])
        dp[node][0] += dp[node_][1]
    dp[node][1] += 1


if __name__ == "__main__":
    N = int(read())
    sns = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, read().split())
        sns[u - 1].append(v - 1)
        sns[v - 1].append(u - 1)
    visited = [False for _ in range(N)]
    dp = [[0, 0] for _ in range(N)]
    cnt = 0
    dfs(0)
    print(min(dp[0][0], dp[0][1]))

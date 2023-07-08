import sys

sys.setrecursionlimit(10**9)
read = sys.stdin.readline

N = int(read())
G = [[] for _ in range(N)]


def DFS(pos, len):
    for i in G[pos]:
        if visited[i[0]] == -1:
            visited[i[0]] = len + i[1]
            DFS(i[0], len + i[1])


for _ in range(N):
    tmp = list(map(int, read().split()))
    for i in range((len(tmp) - 2) // 2):
        G[tmp[0] - 1].append((tmp[i * 2 + 1] - 1, tmp[i * 2 + 2]))

visited = [-1 for _ in range(N)]
visited[0] = 0
DFS(0, 0)

idx = visited.index(max(visited))
visited = [-1 for _ in range(N)]
visited[idx] = 0
DFS(idx, 0)

print(max(visited))

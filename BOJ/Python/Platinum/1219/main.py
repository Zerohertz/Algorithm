import sys
from collections import deque

read = sys.stdin.readline


def bfs(graph, start, end):
    q = deque([start])
    visited = [False for _ in range(len(graph))]
    while q:
        tmp = q.popleft()
        for node, _ in graph[tmp]:
            if not visited[node]:
                if node == end:
                    return True
                visited[node] = True
                q.append(node)
    return False


if __name__ == "__main__":
    N, Start, End, M = map(int, read().split())
    distance = [sys.maxsize for _ in range(N)]
    graph = [[] for _ in range(N)]
    for _ in range(M):
        s, e, p = map(int, read().split())
        graph[s].append([e, p])
    earn = list(map(int, read().split()))
    distance[Start] = -earn[Start]
    for i in range(N):
        for j in range(len(graph[i])):
            graph[i][j][1] -= earn[graph[i][j][0]]
    for _ in range(N - 1):
        for node in range(N):
            for node_, dist_ in graph[node]:
                if (
                    distance[node] != sys.maxsize
                    and distance[node_] > distance[node] + dist_
                ):
                    distance[node_] = distance[node] + dist_
    if distance[End] == sys.maxsize:
        print("gg")
        exit()
    for node in range(N):
        for node_, dist_ in graph[node]:
            if (
                distance[node] != sys.maxsize
                and distance[node_] > distance[node] + dist_
                and bfs(graph, node, End)
            ):
                print("Gee")
                exit()
    print(-distance[End])

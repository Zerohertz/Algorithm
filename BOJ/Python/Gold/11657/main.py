import sys

read = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, read().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, read().split())
        graph[A - 1].append((B - 1, C))
    distance = [sys.maxsize for _ in range(N)]
    distance[0] = 0
    for _ in range(N - 1):
        for node in range(N):
            for node_, dist_ in graph[node]:
                if (
                    distance[node] != sys.maxsize
                    and distance[node] + dist_ < distance[node_]
                ):
                    distance[node_] = distance[node] + dist_
    for node in range(N):
        for node_, dist_ in graph[node]:
            if (
                distance[node] != sys.maxsize
                and distance[node] + dist_ < distance[node_]
            ):
                print(-1)
                exit()
    for i in range(1, N):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])

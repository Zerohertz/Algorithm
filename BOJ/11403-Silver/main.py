import sys

read = sys.stdin.readline


def main():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 0 and (graph[i][k] + graph[k][j] != 2):
                    continue
                graph[i][j] = 1
    for result in graph:
        print(*result)


if __name__ == "__main__":
    N = int(read())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, read().split())))
    main()

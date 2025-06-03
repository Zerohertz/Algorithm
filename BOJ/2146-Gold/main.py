import sys
from collections import deque
from itertools import combinations

read = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):
    queue = deque([(x, y)])
    cluster = []
    if visited[x][y]:
        return cluster
    if maps[x][y] == 1:
        visited[x][y] = True
    cvisited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for dx_, dy_ in zip(dx, dy):
            nx, ny = x + dx_, y + dy_
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny]:
                continue
            if maps[x][y] == 1:
                if maps[nx][ny] == 0:
                    if cvisited[nx][ny]:
                        continue
                    cvisited[nx][ny] = True
                    cluster.append((nx, ny))
                elif maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cluster


def manhattan(c0, c1):
    return abs(c0[0] - c1[0]) + abs(c0[1] - c1[1])


if __name__ == "__main__":
    N = int(read())
    maps = [[] for _ in range(N)]
    for i in range(N):
        maps[i] = list(map(int, read().split()))
    visited = [[False for _ in range(N)] for _ in range(N)]
    cluster = []
    for i in range(N):
        for j in range(N):
            tmp = BFS(i, j)
            if tmp:
                cluster.append(tmp)
    distance = sys.maxsize
    for c1, c2 in combinations(cluster, 2):
        for c1_ in c1:
            for c2_ in c2:
                distance = min(distance, manhattan(c1_, c2_))
    print(distance + 1)

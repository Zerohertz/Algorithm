import math
import sys
from collections import deque

read = sys.stdin.readline


def euclidean(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)


def time(from_, to_):
    if from_ in [0, 1]:
        return distance[from_][to_] / 5
    if distance[from_][to_] > 50:
        return (distance[from_][to_] - 50) / 5 + 2
    return 2


def bfs():
    queue = deque([(0, 0, [0])])
    results = []
    while queue:
        idx, tmp, visited = queue.popleft()
        if idx == 1:
            results.append(tmp)
        else:
            for i in range(N + 2):
                if not i in visited:
                    queue.append((i, tmp + time(idx, i), [*visited, i]))
    return min(results)


if __name__ == "__main__":
    tmp = list(map(float, read().split()))
    tar = list(map(float, read().split()))
    N = int(read())
    coords = [[] for _ in range(N + 2)]
    coords[0], coords[1] = tmp, tar
    for i in range(2, N + 2):
        coords[i] = list(map(float, read().split()))
    distance = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
    for i in range(N + 1):
        for j in range(i + 1, N + 2):
            distance_ = euclidean(coords[i], coords[j])
            distance[i][j] = distance_
            distance[j][i] = distance_
    print(min(euclidean(tmp, tar) / 5, bfs()))

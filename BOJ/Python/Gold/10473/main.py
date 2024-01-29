import heapq
import math
import sys

read = sys.stdin.readline


def euclidean(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)


def _time(distance, from_):
    if from_ == 0:
        return distance / 5
    return min(abs(distance - 50) / 5 + 2, distance / 5)


def dijkstra():
    distance = [sys.maxsize for _ in range(N + 2)]
    distance[0] = 0
    queue = []
    heapq.heappush(queue, (0, 0))
    while queue:
        time_, from_ = heapq.heappop(queue)
        if distance[from_] < time_ or from_ == 1:
            continue
        for to_ in range(1, N + 2):
            distance_ = distance[from_] + time[from_][to_]
            if distance_ < distance[to_]:
                distance[to_] = distance_
                heapq.heappush(queue, (distance_, to_))
    return distance[1]


if __name__ == "__main__":
    tmp = list(map(float, read().split()))
    tar = list(map(float, read().split()))
    N = int(read())
    coords = [[] for _ in range(N + 2)]
    coords[0], coords[1] = tmp, tar
    for i in range(2, N + 2):
        coords[i] = list(map(float, read().split()))
    time = [[sys.maxsize for _ in range(N + 2)] for _ in range(N + 2)]
    for from_ in range(N + 2):
        for to_ in range(N + 2):
            if from_ == to_ or from_ == 1:
                continue
            time[from_][to_] = _time(euclidean(coords[from_], coords[to_]), from_)
    print(dijkstra())

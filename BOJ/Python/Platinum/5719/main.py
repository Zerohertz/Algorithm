import heapq
import sys
from collections import defaultdict

read = sys.stdin.readline


def dijkstra(S, D, opt=False):
    distance = [sys.maxsize for _ in range(N)]
    new_road = [[] for _ in range(N)]
    distance[S] = 0
    queue = [(0, S)]
    while queue:
        distance__, from_ = heapq.heappop(queue)
        if distance[from_] < distance__:
            continue
        for to_, distance_ in road[from_].items():
            if distance_ == sys.maxsize:
                continue
            if distance[from_] + distance_ < distance[to_]:
                distance[to_] = distance[from_] + distance_
                heapq.heappush(queue, (distance[from_] + distance_, to_))
                if opt:
                    new_road[to_] = [from_]
            elif distance[from_] + distance_ == distance[to_]:
                if opt:
                    new_road[to_].append(from_)
    if distance[D] == sys.maxsize:
        return -1, None
    return distance[D], new_road


def dfs(to_=None):
    global visited
    if to_ is None:
        to_ = D
    for from_ in new_road[to_]:
        if not visited[from_]:
            visited[from_] = True
            dfs(from_)
        road[from_][to_] = sys.maxsize


if __name__ == "__main__":
    while True:
        N, M = map(int, read().split())
        if N == 0 and M == 0:
            break
        S, D = map(int, read().split())
        road = [defaultdict(int) for _ in range(N)]
        for _ in range(M):
            U, V, P = map(int, read().split())
            road[U][V] = P
        distance_min, new_road = dijkstra(S, D, True)
        if distance_min == -1:
            print(distance_min)
            continue
        visited = [False for _ in range(N)]
        visited[D] = True
        dfs()
        distance_almost, _ = dijkstra(S, D)
        print(distance_almost)

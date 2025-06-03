"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
72615544	zerohertz	 5719	메모리 초과			Python 3 / 수정	3052	1분 전
"""


import heapq
import sys

read = sys.stdin.readline


def dijkstra_1(S, D):
    distance = [sys.maxsize for _ in range(N)]
    distance[S] = 0
    queue = [S]
    paths = [[] for _ in range(N)]
    while queue:
        from_ = heapq.heappop(queue)
        for to_, distance_ in road[from_]:
            if distance[from_] + distance_ <= distance[to_]:
                distance[to_] = distance[from_] + distance_
                tmp = [path_ for path in paths[from_] for path_ in path]
                if to_ == D:
                    paths[to_].append([*tmp, (from_, to_), distance[to_]])
                else:
                    paths[to_].append([*tmp, (from_, to_)])
                heapq.heappush(queue, to_)
    if distance[D] == sys.maxsize:
        return None, -1
    candidates = list(set([path[-1] for path in paths[D]]))
    candidates.sort()
    if len(candidates) > 1:
        candidates.sort()
        return None, candidates[1]
    banned = []
    for path in paths[D]:
        if path[-1] == candidates[0]:
            banned += path[:-1]
    return banned, None


def dijkstra_2(S, D):
    distance = [sys.maxsize for _ in range(N)]
    distance[S] = 0
    queue = [S]
    while queue:
        from_ = heapq.heappop(queue)
        for to_, distance_ in road[from_]:
            if distance[from_] + distance_ < distance[to_]:
                distance[to_] = distance[from_] + distance_
                heapq.heappush(queue, to_)
    if distance[D] == sys.maxsize:
        return -1
    return distance[D]


if __name__ == "__main__":
    while True:
        N, M = map(int, read().split())
        if N == 0 and M == 0:
            break
        S, D = map(int, read().split())
        road = [[] for _ in range(N)]
        for _ in range(M):
            U, V, P = map(int, read().split())
            road[U].append([V, P])
        paths, distance_min = dijkstra_1(S, D)
        if paths is None:
            print(distance_min)
            continue
        for i, road_i in enumerate(road):
            for j, distance_ in enumerate(road_i):
                if (i, road[i][j][0]) in paths:
                    road[i].remove(road[i][j])
        distance_almost = dijkstra_2(S, D)
        print(distance_almost)

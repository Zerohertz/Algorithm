"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
72607330	zerohertz	 5719	시간 초과			PyPy3 / 수정	2691	1분 전
72607316	zerohertz	 5719	시간 초과			Python 3 / 수정	2691	1분 전
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
            if distance[from_] + distance_ < distance[to_]:
                distance[to_] = distance[from_] + distance_
                paths[to_] = [*paths[from_], (from_, to_)]
                heapq.heappush(queue, to_)
    if distance[D] == sys.maxsize:
        return -1, None
    return paths[D], distance[D]


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
        while True:
            paths, distance_min = dijkstra_1(S, D)
            if paths == -1:
                continue
            for i, road_i in enumerate(road):
                for j, distance_ in enumerate(road_i):
                    if (i, road[i][j][0]) in paths:
                        road[i][j][1] = sys.maxsize
            distance_almost = dijkstra_2(S, D)
            if distance_min == distance_almost:
                continue
            print(distance_almost)
            break

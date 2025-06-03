"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
72618568	zerohertz	 5719	메모리 초과			Python 3 / 수정	3737	9분 전
"""


import heapq
import sys

read = sys.stdin.readline


def dijkstra(S, D):
    distance = [sys.maxsize for _ in range(N)]
    distance[S] = 0
    queue = [(0, S)]
    while queue:
        distance__, from_ = heapq.heappop(queue)
        if distance[from_] < distance__:
            continue
        for to_, distance_ in road[from_]:
            if distance[from_] + distance_ < distance[to_]:
                distance[to_] = distance[from_] + distance_
                heapq.heappush(queue, (distance[from_] + distance_, to_))
    if distance[D] == sys.maxsize:
        return -1
    return distance[D]


def dfs(from_, distance_=0, path=None):
    global banned
    if path is None:
        path = []
    for to_, distance__ in road[from_]:
        if distance_ + distance__ <= distance_min:
            if to_ == D:
                banned += [*path, (from_, to_)]
            dfs(to_, distance_ + distance__, path + [(from_, to_)])


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
        distance_min = dijkstra(S, D)
        banned = []
        dfs(S)
        for i, road_i in enumerate(road):
            for j, distance_ in enumerate(road_i):
                if (i, road[i][j][0]) in banned:
                    road[i].remove(road[i][j])
        distance_almost = dijkstra(S, D)
        print(distance_almost)

"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
72628718	zerohertz	 5719	시간 초과			Python 3 / 수정	1865	1분 전
"""


import heapq
import sys
from collections import defaultdict

read = sys.stdin.readline


def dijkstra(S, D):
    distance = [sys.maxsize for _ in range(N)]
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
    return distance[D]


def dfs(from_, distance_=0, paths=None):
    global visited
    if paths is None:
        paths = []
    for to_, distance__ in road[from_].items():
        if distance_ + distance__ <= distance_min and not visited[to_]:
            if to_ == D:
                road[from_][to_] = sys.maxsize
                for from_, to_ in paths:
                    road[from_][to_] = sys.maxsize
            visited[to_] = True
            dfs(to_, distance_ + distance__, paths + [(from_, to_)])
            visited[to_] = False


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
        distance_min = dijkstra(S, D)
        if distance_min == sys.maxsize:
            print(-1)
            continue
        visited = [False for _ in range(N)]
        visited[S] = True
        dfs(S)
        distance_almost = dijkstra(S, D)
        print(distance_almost)

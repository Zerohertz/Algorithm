"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
73016440	zerohertz	 2887	메모리 초과			Python 3 / 수정	1044	2분 전

정석 MST로 풀었지만 메모리 초과 발생
`N`이 100,000이므로 `maps`를 구성하는 과정에서 발생하는 것으로 예상
이를 메모리 효율적으로 구성하기 위해 모든 노드에 대해 간선을 생성하지 않고 greedy한 접근법이 필요한 것으로 예상
"""

import heapq
import sys
from itertools import combinations

read = sys.stdin.readline


def cost(coord1, coord2):
    return min(
        abs(coord1[0] - coord2[0]),
        abs(coord1[1] - coord2[1]),
        abs(coord1[2] - coord2[2]),
    )


def mst():
    visited = [False for _ in range(N)]
    paths = [(0, 0)]
    cnt = 1
    results = 0
    while paths and cnt <= N:
        weights, from_ = heapq.heappop(paths)
        if visited[from_]:
            continue
        visited[from_] = True
        cnt += 1
        results += weights
        for weights, to_ in maps[from_]:
            if not visited[to_]:
                heapq.heappush(paths, (weights, to_))
    print(results)


if __name__ == "__main__":
    N = int(read())
    coords = [[] for _ in range(N)]
    for i in range(N):
        coords[i] = list(map(int, read().split()))
    maps = [[] for _ in range(N)]
    for i, j in combinations(range(N), 2):
        tmp = cost(coords[i], coords[j])
        maps[i].append((tmp, j))
        maps[j].append((tmp, i))
    mst()

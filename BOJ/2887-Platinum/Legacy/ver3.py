"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
73021914	zerohertz	 2887	메모리 초과			Python 3 / 수정	1111	22초 전


Hash를 통해 `N^2`인 메모리를 `N^2/2`로 감소시켜 도전했지만 이 또한 메모리 초과 발생
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
        for to_ in range(N):
            if not visited[to_] and from_ != to_:
                weights = maps[f"{min(from_, to_)}-{max(from_, to_)}"]
                if not len(paths) or weights < paths[0][0]:
                    heapq.heappush(paths, (weights, to_))
    print(results)


if __name__ == "__main__":
    N = int(read())
    coords = [[] for _ in range(N)]
    for i in range(N):
        coords[i] = list(map(int, read().split()))
    maps = {}
    for i, j in combinations(range(N), 2):
        maps[f"{i}-{j}"] = cost(coords[i], coords[j])
    mst()

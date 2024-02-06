"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
73017719	zerohertz	 2887	메모리 초과			Python 3 / 수정	890	36초 전

메모리를 줄이기 위해 `maps` 자체를 좌표로 두고 `heapq.heappush` 시 `cost`를 계산하는 방법으로 변경
하지만 `heapq.heappush(paths, (cost(from_, to_), to_))` 과정에서 너무 많은 간선이 `paths` 내에 push되어 메모리 초과 발생하는 것으로 예상
`if not visited[to_] and from_ != to_:` 내 조건문을 추가하여 `paths`에 push하는 간선의 수를 줄여 해결할 수 있을 것으로 예상
"""

import heapq
import sys

read = sys.stdin.readline


def cost(from_, to_):
    return min(
        abs(maps[from_][0] - maps[to_][0]),
        abs(maps[from_][1] - maps[to_][1]),
        abs(maps[from_][2] - maps[to_][2]),
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
                heapq.heappush(paths, (cost(from_, to_), to_))
    print(results)


if __name__ == "__main__":
    N = int(read())
    maps = [[] for _ in range(N)]
    for i in range(N):
        maps[i] = list(map(int, read().split()))
    mst()

"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
73011649	zerohertz	 1197	틀렸습니다			Python 3 / 수정	580	2시간 전
"""

import heapq
import sys

read = sys.stdin.readline

if __name__ == "__main__":
    V, E = map(int, read().split())
    edges = []
    for _ in range(E):
        A, B, C = map(int, read().split())
        heapq.heappush(edges, (C, A - 1, B - 1))
    cnt = 1
    results = 0
    visited = [False for _ in range(V)]
    while edges and cnt <= V:
        weights, from_, to_ = heapq.heappop(edges)
        if visited[from_] and visited[to_]:
            continue
        visited[from_] = True
        visited[to_] = True
        cnt += 1
        results += weights
    print(results)

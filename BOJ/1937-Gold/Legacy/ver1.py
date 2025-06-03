"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
86610747	zerohertz	 1937	시간 초과			Python 3 / 수정	979	6분 전

시간 복잡도 O(n^3)이기 때문에 실패
"""

import sys
from collections import deque

read = sys.stdin.readline

Di = (1, 0, -1, 0)
Dj = (0, 1, 0, -1)


def panda(i, j):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque([(i, j, 1)])
    visited[i][j] = True
    bamboo = 0
    while queue:
        i, j, bmb = queue.popleft()
        for di, dj in zip(Di, Dj):
            ni, nj = i + di, j + dj
            if not (0 <= ni < n and 0 <= nj < n):
                continue
            if maps[ni][nj] <= maps[i][j]:
                bamboo = max(bmb, bamboo)
                continue
            visited[ni][nj] = True
            queue.append((ni, nj, bmb + 1))
    return bamboo


def main():
    bamboo = 0
    for i in range(n):
        for j in range(n):
            bamboo = max(bamboo, panda(i, j))
    return bamboo


if __name__ == "__main__":
    n = int(read())
    maps = [[] for _ in range(n)]
    for i in range(n):
        maps[i] = list(map(int, read().split()))
    print(main())

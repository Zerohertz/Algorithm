"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
86612820	zerohertz	 1937	메모리 초과			Python 3 / 수정	1945	52초 전

_maps의 공간 복잡도가 O(n^2*4)여서 실패
O(2*n*(n-1))로 개선해보자
"""

import sys
from collections import deque

read = sys.stdin.readline

Di = (-1, 1, 0, 0)
Dj = (0, 0, -1, 1)
R = {0: 1, 1: 0, 2: 3, 3: 2}


def panda(i, j):
    queue = deque([(i, j, 1)])
    bamboo = 0
    while queue:
        i, j, bmb = queue.popleft()
        for k, (di, dj) in enumerate(zip(Di, Dj)):
            ni, nj = i + di, j + dj
            if not (0 <= ni < n and 0 <= nj < n):
                continue
            if _maps[i][j][k] == -1:
                queue.append((ni, nj, bmb + 1))
            bamboo = max(bmb, bamboo)
    return bamboo


def main():
    bamboo = 0
    for i, j in _init:
        bamboo = max(bamboo, panda(i, j))
    return bamboo


if __name__ == "__main__":
    n = int(read())
    maps = [[] for _ in range(n)]
    for i in range(n):
        maps[i] = list(map(int, read().split()))
    """
    상, 하, 좌, 우
    -1 -> 이동 불가
    0 -> ==
    1 -> 이동 가능
    """
    _maps = [[[-10 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k, (di, dj) in enumerate(zip(Di, Dj)):
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < n):
                    continue
                if _maps[ni][nj][k] != -10:
                    continue
                if maps[i][j] < maps[ni][nj]:
                    _maps[i][j][k] = 1
                    _maps[ni][nj][R[k]] = -1
                elif maps[i][j] > maps[ni][nj]:
                    _maps[i][j][k] = -1
                    _maps[ni][nj][R[k]] = 1
                else:
                    _maps[i][j][k] = _maps[ni][nj][R[k]] = 0
    _init = []
    for i in range(n):
        for j in range(n):
            status = True
            for k in range(4):
                if _maps[i][j][k] == 1:
                    status = False
                    break
            if status:
                _init.append((i, j))
    print(main())

import sys
from collections import defaultdict

read = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(tmp, weight):
    if tmp == end:
        return weight
    __weight = 0
    for _tmp, _weight in bridges[tmp].items():
        if visited[_tmp]:
            continue
        visited[_tmp] = True
        __weight = max(__weight, dfs(_tmp, min(weight, _weight)))
        visited[_tmp] = False
    return __weight


def main():
    visited[start] = True
    return dfs(start, sys.maxsize)


if __name__ == "__main__":
    N, M = map(int, read().split())
    bridges = [defaultdict(int) for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, read().split())
        bridges[A - 1][B - 1] = max(bridges[A - 1][B - 1], C)
        bridges[B - 1][A - 1] = max(bridges[B - 1][A - 1], C)
    start, end = map(int, read().split())
    start -= 1
    end -= 1
    visited = [False for _ in range(N)]
    print(main())

import sys
from collections import defaultdict, deque

read = sys.stdin.readline


def bfs(weight):
    visited = [False for _ in range(N)]
    visited[start] = True
    queue = deque([start])
    while queue:
        tmp = queue.popleft()
        if tmp == end:
            return True
        for _tmp, _weight in bridges[tmp].items():
            if visited[_tmp] or _weight < weight:
                continue
            visited[_tmp] = True
            queue.append(_tmp)
    return False


def main():
    left, right = 1, 1_000_000_000
    while left <= right:
        mid = (left + right) // 2
        if bfs(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right


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
    print(main())

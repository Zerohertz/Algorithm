import sys
from collections import deque

read = sys.stdin.readline

dx = [1, -1, -1, 1, 1, 0, -1, 0]
dy = [1, 1, -1, -1, 0, 1, 0, -1]


def BFS():
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if not maps[nx][ny]:
                maps[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))
    return cnt


if __name__ == "__main__":
    N, M = map(int, read().split())
    maps = []
    queue = deque()
    for i in range(N):
        tmp = list(map(int, read().split()))
        for j, value in enumerate(tmp):
            if value == 1:
                queue.append((i, j, 0))
        maps.append(tmp)
    print(BFS())

import sys
from collections import deque

read = sys.stdin.readline

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def melt():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = True
    maps[0][0] = 3
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for dx_, dy_ in zip(dx, dy):
            nx, ny = x + dx_, y + dy_
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if maps[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
            else:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                elif visited[nx][ny] == 1:
                    visited[nx][ny] = 2
                    maps[nx][ny] = 0


def done():
    status = True
    for maps_ in maps:
        for maps__ in maps_:
            if maps__ == 1:
                status = False
    return status


if __name__ == "__main__":
    N, M = map(int, read().split())
    maps = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        maps[i] = list(map(int, read().split()))
    cnt = 0
    while not done():
        melt()
        cnt += 1
    print(cnt)

import sys
from collections import deque

read = sys.stdin.readline


def BFS(i, j):
    dx = [1, -1, -1, 1, 1, 0, -1, 0]
    dy = [1, 1, -1, -1, 0, 1, 0, -1]
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[i][j] = True
    queue = deque([(i, j, 0)])
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if maps[nx][ny] == 1:
                return cnt + 1
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))


if __name__ == "__main__":
    N, M = map(int, read().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, read().split())))
    result = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                continue
            result = max(result, BFS(i, j))
    print(result)

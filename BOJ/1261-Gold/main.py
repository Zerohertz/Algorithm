import sys
from collections import deque

read = sys.stdin.readline


def main(maze, M, N):
    if M == 1 and N == 1:
        return 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    queue = deque([(0, 0, 0)])
    visited = [[sys.maxsize for _ in range(M)] for _ in range(N)]
    while queue:
        x, y, cnt = queue.popleft()
        for _dx, _dy in zip(dx, dy):
            nx, ny = x + _dx, y + _dy
            if 0 <= nx < N and 0 <= ny < M and cnt < visited[nx][ny]:
                if nx == N - 1 and ny == M - 1:
                    return cnt
                if maze[nx][ny] == 0:
                    queue.appendleft((nx, ny, cnt))
                    visited[nx][ny] = cnt
                elif cnt + 1 < visited[nx][ny]:
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = cnt + 1
    return visited[-1][-1]


if __name__ == "__main__":
    M, N = map(int, read().strip().split())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, read().strip())))
    print(main(maze, M, N))

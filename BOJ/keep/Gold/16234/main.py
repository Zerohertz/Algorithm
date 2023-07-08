import sys
from collections import deque


def BFS(A, ix, iy):
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    q = deque([(ix, iy)])
    tmp = deque([(ix, iy)])
    Visited[ix][iy] = True
    value = A[ix][iy]
    cnt = 1
    while q:
        tx, ty = q.popleft()
        for i, j in zip(x, y):
            nx, ny = tx + i, ty + j
            if 1 <= nx <= N and 1 <= ny <= N and not Visited[nx][ny]:
                if L <= abs(A[tx][ty] - A[nx][ny]) <= R:
                    value += A[nx][ny]
                    cnt += 1
                    q.append((nx, ny))
                    tmp.append((nx, ny))
                    Visited[nx][ny] = True
    while tmp:
        nx, ny = tmp.popleft()
        A[nx][ny] = int(value / cnt)
    if cnt == 1:
        return 0
    else:
        return 1


if __name__ == "__main__":
    read = sys.stdin.readline
    N, L, R = map(int, read().split())
    A = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    i = 1
    for r in range(1, N + 1):
        l = list(map(int, read().split()))
        for c, a in enumerate(l):
            A[r][c + 1] = a
            i += 1
    Day = 0
    while True:
        Visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
        flag = 0
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                if not Visited[r][c]:
                    flag += BFS(A, r, c)
        if flag == 0:
            print(Day)
            break
        Day += 1

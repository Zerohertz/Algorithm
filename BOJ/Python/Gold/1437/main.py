import sys
from collections import deque

read = sys.stdin.readline


def man(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def BFS():
    q = deque([(hx, hy)])
    while q:
        x, y = q.popleft()
        if man(x, y, tx, ty) <= 1000:
            print("happy")
            return
        for i in range(N):
            if not visited[i]:
                nx, ny = pyeon[i]
                if man(x, y, nx, ny) <= 1000:
                    q.append((nx, ny))
                    visited[i] = True
    print("sad")
    return


if __name__ == "__main__":
    T = int(read())
    for _ in range(T):
        N = int(read())
        hx, hy = map(int, read().split())
        pyeon = []
        for _ in range(N):
            x, y = map(int, read().split())
            pyeon.append((x, y))
        tx, ty = map(int, read().split())
        visited = [False for _ in range(N + 1)]
        BFS()

import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())
l = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    l[i] = list(map(int, list(read().rstrip())))

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]


def BFS():
    q = deque([(0, 0, 1)])
    while q:
        x, y, cnt = q.popleft()
        for i, j in zip(v1, v2):
            if 0 <= x + i < N and 0 <= y + j < M:
                if l[x + i][y + j] == 1:
                    q.append((x + i, y + j, cnt + 1))
                    l[x + i][y + j] = cnt + 1


BFS()
print(l[N - 1][M - 1])

import copy
import sys
from itertools import product

read = sys.stdin.readline

N = int(read())
sav = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    sav[i] = list(map(int, read().split()))


def n2n(i, j, dir):
    while True:
        if not (((0 <= i < N) and (0 <= j < N)) and (
                (0 <= i + dir[1] < N) and (0 <= j + dir[0] < N))):
            break
        elif not G[i][j] == 0:
            if G[i + dir[1]][j + dir[0]
                             ] == G[i][j] and not visited[i + dir[1]][j + dir[0]]:
                G[i + dir[1]][j + dir[0]] = G[i][j] * 2
                G[i][j] = 0
                visited[i + dir[1]][j + dir[0]] = True
                break
            elif G[i + dir[1]][j + dir[0]] == 0:
                G[i + dir[1]][j + dir[0]] = G[i][j]
                G[i][j] = 0
                i, j = i + dir[1], j + dir[0]
            else:
                break
        else:
            break


dir_t = ((1, 0), (0, -1), (-1, 0), (0, 1))
x_r = ((N - 2, -1, -1), (0, N, 1), (1, N, 1), (0, N, 1))
y_r = ((0, N, 1), (1, N, 1), (0, N, 1), (N - 2, -1, -1))


def simulation(dir):  # 0, 1, 2, 3
    dir_x, dir_y = dir_t[dir]
    for i in range(y_r[dir][0], y_r[dir][1], y_r[dir][2]):
        for j in range(x_r[dir][0], x_r[dir][1], x_r[dir][2]):
            n2n(i, j, dir_t[dir])


res = 0

for a, b, c, d, e in product(range(4), range(4), range(4), range(4), range(4)):
    G = copy.deepcopy(sav)
    visited = [[False for _ in range(N)] for _ in range(N)]
    simulation(a)
    visited = [[False for _ in range(N)] for _ in range(N)]
    simulation(b)
    visited = [[False for _ in range(N)] for _ in range(N)]
    simulation(c)
    visited = [[False for _ in range(N)] for _ in range(N)]
    simulation(d)
    visited = [[False for _ in range(N)] for _ in range(N)]
    simulation(e)
    res = max(max(map(max, G)), res)
print(res)

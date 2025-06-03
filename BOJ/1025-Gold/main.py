import math
import sys

read = sys.stdin.readline


def check(M, x, y, dx, dy):
    res = -1
    tmp = ""
    if dx == 0 and dy == 0:
        t = M[x][y]
        ts = math.sqrt(t)
        if ts == int(ts):
            res = t
    else:
        while True:
            if 0 <= x < n and 0 <= y < m:
                tmp += str(M[x][y])
                t = int(tmp)
                ts = math.sqrt(t)
                if ts == int(ts):
                    res = t
                x += dx
                y += dy
            else:
                break
    return res


if __name__ == "__main__":
    n, m = map(int, read().split())
    Map = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        tmp = read().strip()
        for j, t in enumerate(tmp):
            Map[i][j] = int(t)
    RES = -1
    for x in range(n):
        for y in range(m):
            for dx in range(-n + 1, n):
                for dy in range(-m + 1, m):
                    RES = max(RES, check(Map, x, y, dx, dy))
    print(RES)

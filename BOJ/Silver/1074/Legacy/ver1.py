import sys

read = sys.stdin.readline

tmp = [0]


def zzz(x, y, n):
    if n != 2:
        for tmpx in range(x, x + n):
            for tmpy in range(y, y + n):
                zzz(x, y, n // 2)
                zzz(x, y + n // 2, n // 2)
                zzz(x + n // 2, y, n // 2)
                zzz(x + n // 2, y + n // 2, n // 2)
                return
    else:
        for tmpx in range(x, x + n):
            for tmpy in range(y, y + n):
                l[tmpx][tmpy] = tmp[0]
                tmp[0] += 1


N, c, r = map(int, read().split())
l = [[-1 for _ in range(2 ** N)] for _ in range(2 ** N)]

zzz(0, 0, 2 ** N)
print(l[c][r])

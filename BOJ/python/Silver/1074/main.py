import sys

read = sys.stdin.readline


def zzz(N, r, c):
    if N == 0:
        return 0
    else:
        return 2 * (r % 2) + (c % 2) + 4 * zzz(N - 1, r // 2, c // 2)


N, r, c = map(int, read().split())
print(zzz(N, r, c))

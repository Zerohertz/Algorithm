import sys

read = sys.stdin.readline

N = int(read())
A = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    A[i + 1] = [0] + list(map(int, read().split()))


def election(x, y, d1, d2):
    e = [0 for _ in range(5)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if x + y <= i + j <= x + y + 2 * d2 and x - y <= i - j <= x - y + 2 * d1:
                e[4] += A[i][j]
            elif 1 <= i < x + d1 and 1 <= j <= y:
                e[0] += A[i][j]
            elif 1 <= i <= x + d2 and y <= j <= N:
                e[1] += A[i][j]
            elif x + d1 <= i <= N and 1 <= j < y - d1 + d2:
                e[2] += A[i][j]
            elif x + d2 <= i <= N and y - d1 + d2 <= j <= N:
                e[3] += A[i][j]
    return max(e) - min(e)


res = sys.maxsize
for d1 in range(1, N):
    for d2 in range(1, N):
        for x in range(N):
            for y in range(N):
                res = min(res, election(x, y, d1, d2))

print(res)

import sys

read = sys.stdin.readline


def splitPaper(x, y, n):
    c = l[x][y]
    for tmpx in range(x, x + n):
        for tmpy in range(y, y + n):
            if c != l[tmpx][tmpy]:
                splitPaper(x, y, n // 2)
                splitPaper(x + n // 2, y, n // 2)
                splitPaper(x, y + n // 2, n // 2)
                splitPaper(x + n // 2, y + n // 2, n // 2)
                return
    if c == 0:
        res.append(0)
    else:
        res.append(1)


N = int(read())
l = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    l[i] = list(map(int, read().split()))

res = []
splitPaper(0, 0, N)
print(res.count(0))
print(res.count(1))

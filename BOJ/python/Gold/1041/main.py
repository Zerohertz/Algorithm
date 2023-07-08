import sys
from itertools import combinations

read = sys.stdin.readline

N = int(read())
l = list(map(int, read().split()))
if N == 1:
    print(sum(l) - max(l))
else:
    d1 = min(l)

    exceptList = ((0, 5), (1, 4), (2, 3))
    tmp = list(combinations(range(6), 2))
    for i in exceptList:
        tmp.remove(i)

    d2 = sys.maxsize
    for i in tmp:
        d2 = min(d2, l[i[0]] + l[i[1]])

    tmp = (
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 4),
        (0, 3, 4),
        (5, 1, 2),
        (5, 1, 3),
        (5, 2, 4),
        (5, 3, 4),
    )

    d3 = sys.maxsize
    for i in tmp:
        d3 = min(d3, l[i[0]] + l[i[1]] + l[i[2]])

    d2n = (N - 1) * 4 + (N - 2) * 4
    d3n = 4
    d1n = N**3 - ((N - 1) * (N - 2) * (N - 2)) - d2n - d3n

    print(d1 * d1n + d2 * d2n + d3 * d3n)

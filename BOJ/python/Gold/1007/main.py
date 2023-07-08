import math
import sys
from itertools import combinations

read = sys.stdin.readline

T = int(read())

for _ in range(T):
    N = int(read())
    xt = 0
    yt = 0
    P = [[0, 0] for _ in range(N)]
    for i in range(N):
        P[i] = list(map(int, read().split()))
        xt += P[i][0]
        yt += P[i][1]
    comb = list(combinations(P, int(N / 2)))
    l = int(len(comb) / 2)
    res = sys.maxsize
    for i in comb[:l]:
        i = list(i)
        x1t, y1t = 0, 0
        for x, y in i:
            x1t += x
            y1t += y
        x2t, y2t = xt - x1t, yt - y1t
        res = min(res, math.sqrt((x2t - x1t) ** 2 + (y2t - y1t) ** 2))
    print(res)

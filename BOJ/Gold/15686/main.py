import sys
from itertools import combinations

read = sys.stdin.readline

N, M = map(int, read().split())
l = [[0 for _ in range(N)] for _ in range(N)]
chickenhouse = []
house = []
for i in range(N):
    l[i] = list(map(int, read().split()))
    for j in range(N):
        if l[i][j] == 1:
            house.append((i, j))
        elif l[i][j] == 2:
            chickenhouse.append((i, j))


def distance(t1, t2):
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])


res = sys.maxsize
for tmpchickenhouse in combinations(chickenhouse, M):
    tmp = 0
    for tmphouse in house:
        nd = sys.maxsize
        for nch in tmpchickenhouse:
            nd = min(nd, distance(nch, tmphouse))
        tmp += nd
    res = min(res, tmp)

print(res)

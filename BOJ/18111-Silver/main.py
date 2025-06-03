import sys

read = sys.stdin.readline

N, M, B = map(int, read().split())
l = [list(map(int, read().split())) for _ in range(N)]

mt = sys.maxsize
Mh = 0
for i in range(257):
    maxtar, mintar = 0, 0
    for j in range(N):
        for k in range(M):
            if l[j][k] >= i:
                maxtar += l[j][k] - i
            else:
                mintar += i - l[j][k]
    if maxtar + B >= mintar:
        if mintar + maxtar * 2 <= mt:
            mt = mintar + maxtar * 2
            Mh = i

print(mt, Mh)

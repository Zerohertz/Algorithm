import sys

read = sys.stdin.readline

N, M = map(int, read().split())
l = list(map(int, read().split()))

tmp = 0
res = 0
idx2 = 0

for idx1 in range(N):
    while tmp < M and idx2 < N:
        tmp += l[idx2]
        idx2 += 1
    if tmp == M:
        res += 1
    tmp -= l[idx1]

print(res)

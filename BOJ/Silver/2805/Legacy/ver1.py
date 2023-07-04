import sys

read = sys.stdin.readline

N, M = map(int, read().split())
l = list(map(int, read().split()))

tmp = max(l) - 1
res = 0
while res < M:
    res = 0
    for i in range(N):
        if l[i] > tmp:
            res += l[i] - tmp
    tmp -= 1
print(tmp + 1)

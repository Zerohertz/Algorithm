import sys
from itertools import combinations

read = sys.stdin.readline

N, S = map(int, read().split())
l = list(map(int, read().split()))

res = 0
for i in range(1, N + 1):
    for j in combinations(l, i):
        if sum(j) == S:
            res += 1

print(res)

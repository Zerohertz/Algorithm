import sys
from itertools import combinations

read = sys.stdin.readline

L = int(read())
S = list(map(int, read().split()))
n = int(read())

if n in S:
    print(0)
    exit()

S.append(n)
S.sort()
tmp = S.index(n)

res = 0
if tmp == 0:
    for i in combinations(range(1, S[tmp + 1]), 2):
        if i[0] <= n <= i[1]:
            res += 1
else:
    for i in combinations(range(S[tmp - 1] + 1, S[tmp + 1]), 2):
        if i[0] <= n <= i[1]:
            res += 1

print(res)

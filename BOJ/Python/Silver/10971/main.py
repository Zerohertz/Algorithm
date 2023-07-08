import sys
from itertools import permutations

read = sys.stdin.readline

N = int(read())
l = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    l[i] = list(map(int, read().split()))

res = sys.maxsize
for i in permutations(range(N)):
    tmp = 0
    status = True
    for j in range(N):
        tmp += l[i[j - 1]][i[j]]
        if l[i[j - 1]][i[j]] == 0:
            status = False
            break
    if status:
        res = min(res, tmp)

print(res)

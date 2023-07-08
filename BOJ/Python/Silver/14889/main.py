import sys
from itertools import combinations, permutations

read = sys.stdin.readline

N = int(read())
l = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    l[i] = list(map(int, read().split()))

res = sys.maxsize
for start in combinations(range(N), N // 2):
    link = set(range(N)) - set(start)
    start_score, link_score = 0, 0
    for i in permutations(start, 2):
        start_score += l[i[0]][i[1]]
    for i in permutations(link, 2):
        link_score += l[i[0]][i[1]]
    res = min(res, abs(start_score - link_score))

print(res)

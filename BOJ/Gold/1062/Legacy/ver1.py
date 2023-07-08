import sys
from itertools import combinations

read = sys.stdin.readline

N, K = map(int, read().split())

s = set()
wordset = []
antic = set("antic")
tupleantic = tuple(antic)

for i in range(N):
    word = read().rstrip()
    tmpwordset = set(word) - antic
    s |= tmpwordset
    wordset.append(tmpwordset)

res = 0
if K > 5:
    for i in combinations(s, K - 5):
        tmp = 0
        tmpi = tupleantic + i
        for j in wordset:
            if j - set(tmpi) == set():
                tmp += 1
        res = max(res, tmp)
elif K == 5:
    tmp = 0
    for j in wordset:
        if j - set(antic) == set():
            tmp += 1
    res = tmp

print(res)

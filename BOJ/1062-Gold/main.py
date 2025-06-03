import sys
from itertools import combinations

read = sys.stdin.readline

N, K = map(int, read().split())

s = set()
wordset = []
antic = set("antic")

for i in range(N):
    word = read().rstrip()
    tmpwordset = set(word)
    wordset.append(tmpwordset)

s = set(chr(i) for i in range(ord("a"), ord("z") + 1)) - antic

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    res = 0
    l = [False for _ in range(26)]
    for ch in antic:
        l[ord(ch) - ord("a")] = True
    for teach in combinations(s, K - 5):
        tmp = 0
        for t in teach:
            l[ord(t) - ord("a")] = True
        for word in wordset:
            status = True
            for w in word:
                if not l[ord(w) - ord("a")]:
                    status = False
                    break
            if status:
                tmp += 1
        for t in teach:
            l[ord(t) - ord("a")] = False
        res = max(res, tmp)
    print(res)

import sys
from itertools import combinations

s = sys.stdin.readline().rstrip()


def swap(s, idx1, idx2):
    tmp = s[idx2]
    s = s[:idx2] + s[idx1] + s[idx2 + 1:]
    s = s[:idx1] + tmp + s[idx1 + 1:]
    return s


def Palindrome(s, idx1, idx2):
    if cache[idx1][idx2] != -1:
        return cache[idx1][idx2]
    while idx1 < idx2:
        if s[idx1] == s[idx2]:
            idx1 += 1
            idx2 -= 1
        else:
            break
    if idx1 >= idx2:
        return 0
    res = min(
        Palindrome(s, idx1 + 1, idx2) + 1,
        Palindrome(s, idx1, idx2 - 1) + 1,
        Palindrome(s, idx1 + 1, idx2 - 1) + 1,
    )
    cache[idx1][idx2] = res
    return res


l = len(s)
com = list(combinations([i for i in range(l)], 2))
ans = sys.maxsize
cache = [[-1 for _ in range(51)] for _ in range(51)]
ans = min(ans, Palindrome(s, 0, l - 1))
for c1, c2 in com:
    cache = [[-1 for _ in range(51)] for _ in range(51)]
    tmps = swap(s, c1, c2)
    ans = min(ans, Palindrome(tmps, 0, l - 1) + 1)
print(ans)

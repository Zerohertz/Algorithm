# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque

from extratypes import Tree  # library with types used in the task


def solution(T):
    q = deque([(T, 0)])
    res = 0
    while q:
        tmp, h = q.popleft()
        for i in [tmp.l, tmp.r]:
            if not i is None:
                q.append((i, h + 1))
                res = max(res, h + 1)
    return res

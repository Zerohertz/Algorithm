# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

def solution(A):
    # write your code in Python 3.8.10
    cnt = Counter(A)
    for i in cnt:
        if cnt[i] == 1:
            return i
    return -1
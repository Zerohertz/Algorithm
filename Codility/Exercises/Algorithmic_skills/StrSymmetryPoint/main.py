# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # write your code in Python 3.8.10
    N = len(S)
    res = 0
    for i in range(N // 2):
        if S[i] == S[N - i - 1]:
            res += 1
        else:
            return -1
    if N % 2 == 0:
        return -1
    else:
        return res

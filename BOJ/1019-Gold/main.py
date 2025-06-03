import sys

read = sys.stdin.readline

"""
def brute_forece(N):
    res = [0 for _ in range(10)]
    for i in range(1, N + 1):
        for j in str(i):
            res[int(j)] += 1
    for r in res:
        print(r, end=" ")
"""


if __name__ == "__main__":
    N = int(read())
    # brute_forece(N)

    tmp = 1
    res = [0 for _ in range(10)]
    while N > 0:
        while N % 10 != 9:
            for i in str(N):
                res[int(i)] += tmp
            N -= 1
        if N < 10:
            for i in range(N + 1):
                res[i] += tmp
        else:
            for i in range(10):
                res[i] += (N // 10 + 1) * tmp
        res[0] -= tmp
        tmp *= 10
        N //= 10
    for r in res:
        print(r, end=" ")

import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N = int(read())
    k = int(read())

    """
    # A = [[(i + 1) * (j + 1) for j in range(N)] for i in range(N)]
    A = [(i + 1) * (j + 1) for j in range(N) for i in range(N)]
    B = sorted(A)
    print(B[k])
    """

    left, right = 1, k
    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        for i in range(1, N + 1):
            tmp += min(mid // i, N)
        if tmp >= k:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    print(res)

"""
1 2 3
2 4 6
3 6 9

1 2 2 3 3 4 `6` 6 9

7 // 3 -> 2
7 % 3 -> 1


1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
"""

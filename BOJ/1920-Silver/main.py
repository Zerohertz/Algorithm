import sys

read = sys.stdin.readline


def bisect(b):
    left, right = 0, N - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] < b:
            left = mid + 1
        else:
            right = mid
    return left


def main():
    A.sort()
    for b in B:
        print(int(A[bisect(b)] == b))


if __name__ == "__main__":
    N = int(read())
    A = list(map(int, read().split()))
    M = int(read())
    B = list(map(int, read().split()))
    main()


"""1st
def binary(A, n, tar):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == tar:
            return True
        if tar < A[mid]:
            right = mid - 1
        elif tar > A[mid]:
            left = mid + 1


N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in range(M):
    if binary(A, N, B[i]):
        print(1)
    else:
        print(0)
"""

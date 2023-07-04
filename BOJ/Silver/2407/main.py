import sys

read = sys.stdin.readline


def factorial(m, n):
    res = 1
    for i in range(m, n + 1):
        res *= i
    return res


n, m = map(int, read().split())
if n // 2 >= m:
    print(factorial(n - m + 1, n) // factorial(1, m))
else:
    print(factorial(m + 1, n) // factorial(1, n - m))

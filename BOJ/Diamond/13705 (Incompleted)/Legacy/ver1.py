import math
import sys


def f(A, B, C, x):
    return C - A * x - B * math.sin(x)


def fp(A, B, x):
    return - A - B * math.cos(x)


def newrap(A, B, C, x):
    return x - f(A, B, C, x) / fp(A, B, x)


read = sys.stdin.readline
A, B, C = map(int, read().split())

tmp = C / A

for i in range(3000):
    tmp = newrap(A, B, C, tmp)

print(round(tmp, 6))

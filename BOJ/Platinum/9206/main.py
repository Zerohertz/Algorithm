import math
import sys


def f(a, b, h, x):
    return a * math.e ** (- ((x) ** 2)) + b * x ** (0.5)


def integration(a, b, h):
    V = 0
    resolution = 100001
    resol = resolution - 1
    for i in range(1, resolution):
        befx = (i - 1) / resol * h
        tmpx = i / resol * h
        tmpy = (f(a, b, h, befx) + f(a, b, h, tmpx)) / 2
        V += tmpy ** 2 * math.pi / resol * h
    return V


read = sys.stdin.readline

V, N = map(float, read().split())
res = []
for i in range(int(N)):
    a, b, h = map(float, read().split())
    res.append([abs(integration(a, b, h) - V), i])

res.sort(key=lambda x: x[0])
print(res[0][1])

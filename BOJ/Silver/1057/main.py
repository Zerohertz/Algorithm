import sys

read = sys.stdin.readline

N, A, B = map(int, read().split())

res = 1

while N > 1:
    if N % 2 == 0:
        N = N // 2
    else:
        N = N // 2 + 1
    A = round(A / 2 + 0.01)
    B = round(B / 2 + 0.01)
    if A == B:
        break
    res += 1

print(res)

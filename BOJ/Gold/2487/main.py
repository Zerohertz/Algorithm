import sys

read = sys.stdin.readline

N = int(read())
l = [0] + list(map(int, read().split())) + [0 for _ in range(20_000)]
v = [False for _ in range(20_007)]


def GCD(B, A):
    while A != 0:
        C = B % A
        B = A
        A = C
    return B


def LCM(A, B):
    return A / GCD(A, B) * B


def checkCycle(start):
    cnt = 1
    next = l[start]
    while True:
        if start == next:
            return cnt
        v[next] = True
        next = l[next]
        cnt += 1


res = 1
for i in range(1, N + 1):
    if not v[i]:
        res = LCM(res, checkCycle(i))
print(int(res))

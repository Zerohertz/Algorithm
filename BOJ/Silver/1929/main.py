import sys


def returnPN(M, N):
    l = []
    for i in range(M, N + 1):
        if i == 1:
            continue
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            l.append(i)
    return l


read = sys.stdin.readline

M, N = map(int, read().split())

l = returnPN(M, N)
for i in l:
    print(i)

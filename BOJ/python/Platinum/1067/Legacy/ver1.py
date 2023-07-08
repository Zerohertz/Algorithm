import sys

read = sys.stdin.readline

N = int(read())

X = list(map(int, read().split()))
Y = list(map(int, read().split()))

M = 0
tmp = 0
for i in range(N):
    tmp = 0
    for j in range(N):
        tmp += X[(i + j) % N] * Y[j]
    if M < tmp:
        M = tmp
print(M)

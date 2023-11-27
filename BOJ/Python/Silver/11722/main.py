import sys

read = sys.stdin.readline

N = int(read())
A = list(map(int, read().split()))
res = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            res[i] = max(res[i], res[j] + 1)

print(max(res))

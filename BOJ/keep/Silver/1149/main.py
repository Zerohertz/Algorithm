import sys

read = sys.stdin.readline

N = int(read())
C = [[0, 0, 0] for i in range(N)]

for i in range(N):
    C[i][0], C[i][1], C[i][2] = map(int, read().split())

for i in range(1, N):
    C[i][0] += min(C[i - 1][1], C[i - 1][2])
    C[i][1] += min(C[i - 1][0], C[i - 1][2])
    C[i][2] += min(C[i - 1][0], C[i - 1][1])

print(min(C[N - 1][0], C[N - 1][1], C[N - 1][2]))

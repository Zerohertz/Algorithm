import sys

read = sys.stdin.readline

N = int(read())
T, P = [0 for _ in range(N)], [0 for _ in range(N)]

for i in range(N):
    T[i], P[i] = map(int, read().split())

V = [0 for _ in range(N + 1)]
for i in range(N - 1, -1, -1):
    if T[i] + i <= N:
        V[i] = max(P[i] + V[i + T[i]], V[i + 1])
    else:
        V[i] = V[i + 1]

print(V[0])

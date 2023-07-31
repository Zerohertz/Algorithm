N, K = map(int, input().split())

W = [0 for _ in range(N + 1)]
V = [0 for _ in range(N + 1)]
info = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N):
    W[i], V[i] = map(int, input().split())

for i in range(N + 1):
    for j in range(K + 1):
        w = W[i]
        v = V[i]
        if j < w:
            info[i][j] = info[i - 1][j]
        else:
            info[i][j] = max(info[i - 1][j], info[i - 1][j - w] + v)

print(info[N][K])

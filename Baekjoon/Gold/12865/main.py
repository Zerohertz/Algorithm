N, K = map(int, input().split())

W = []
V = []
info = [[0] * (K + 1) for _ in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    W.append(a)
    V.append(b)

for i in range(N):
    for j in range(K + 1):
        w = W[i]
        v = V[i]
        if j < w:
            info[i][j] = info[i - 1][j]
        else:
            info[i][j] = max(info[i - 1][j], info[i - 1][j - w] + v)

print(info[N - 1][K])
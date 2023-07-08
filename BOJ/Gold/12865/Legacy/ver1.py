N, K = map(int, input().split())

W = []
V = []
Vlist = []

for i in range(N):
    a, b = map(int, input().split())
    W.append(a)
    V.append(b)

for i in range(2**N):
    tmpbin = bin(i)
    tmpb = tmpbin[2:]
    binidx = [tmpb[j] for j in range(len(tmpb))]
    idx = ["0" for j in range(N)]
    idx[N - len(binidx) :] = binidx
    totW = 0
    totV = 0
    for j in range(N):
        if idx[j] == "1":
            totW = totW + W[j]
            totV = totV + V[j]
    if totW <= K:
        Vlist.append(totV)

print(max(Vlist))

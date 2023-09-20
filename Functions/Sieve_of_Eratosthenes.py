def SoE(N):
    B = [False, False] + [True] * (N - 1)
    PN = []
    for i in range(2, N + 1):
        if B[i]:
            PN.append(i)
            for j in range(2 * i, N + 1, i):
                B[j] = False
    return PN

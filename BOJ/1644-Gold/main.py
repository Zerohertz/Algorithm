import sys

read = sys.stdin.readline


def SoE(N):
    B = [False, False] + [True] * (N - 1)
    PN = []
    for i in range(2, N + 1):
        if B[i]:
            PN.append(i)
            for j in range(2 * i, N + 1, i):
                B[j] = False
    return PN


if __name__ == "__main__":
    N = int(read())
    PN = SoE(N)
    cnt = 0
    p1 = 0
    p2 = 0
    while p2 <= len(PN):
        tmp = sum(PN[p1:p2])
        if tmp == N:
            cnt += 1
            p2 += 1
        elif tmp < N:
            p2 += 1
        else:
            p1 += 1
    print(cnt)

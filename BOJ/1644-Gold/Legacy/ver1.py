import sys

read = sys.stdin.readline


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


if __name__ == "__main__":
    N = int(read())
    PN = returnPN(1, N)
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

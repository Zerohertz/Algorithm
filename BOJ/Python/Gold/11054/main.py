import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N = int(read())
    A = list(map(int, read().split()))
    B = A[::-1]
    res1 = [1 for _ in range(N)]
    res2 = [1 for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                res1[i] = max(res1[i], res1[j] + 1)
            if B[i] > B[j]:
                res2[i] = max(res2[i], res2[j] + 1)

    cnt = 0
    for i in range(N):
        cnt = max(cnt, res1[i] + res2[N - i - 1] - 1)
    print(cnt)

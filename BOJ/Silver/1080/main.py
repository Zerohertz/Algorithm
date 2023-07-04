import sys

read = sys.stdin.readline


def cal(mat, x, y):
    for i in range(3):
        for j in range(3):
            if mat[x + i][y + j] == '1':
                mat[x + i][y + j] = '0'
            else:
                mat[x + i][y + j] = '1'


N, M = map(int, read().split())
A = [[] for _ in range(N)]
B = [[] for _ in range(N)]

for i in range(N):
    A[i] = list(read().rstrip())

for i in range(N):
    B[i] = list(read().rstrip())

cnt = 0

for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            cal(A, i, j)
            cnt += 1

status = True

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            status = False
            break

if status:
    print(cnt)
else:
    print(-1)

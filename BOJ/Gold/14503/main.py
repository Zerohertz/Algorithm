import sys

read = sys.stdin.readline

N, M = map(int, read().split())
r, c, d = map(int, read().split())

l = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    l[i] = list(map(int, read().split()))

res = 1
visit = [[False for _ in range(M)] for _ in range(N)]
visit[r][c] = True
dirdict = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
while True:
    status = False
    for i in range(4):  # 2.
        d = (d + 3) % 4  # 2.2.
        y, x = dirdict[d]
        if 0 <= r + x < N and 0 <= c + y < M:  # 2.1.
            if not visit[r + x][c + y] and l[r + x][c + y] == 0:
                r, c = r + x, c + y
                res += 1
                visit[r][c] = True
                status = True
                break
    if status:
        continue
    if 0 <= r - x < N and 0 <= c - y < M:
        if l[r - x][c - y] == 0:  # 2.3.
            r, c = r - x, c - y
        else:  # 2.4.
            break

print(res)

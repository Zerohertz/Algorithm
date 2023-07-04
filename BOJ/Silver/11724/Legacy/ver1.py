import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())

l = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = map(int, read().split())
    l[a - 1][b - 1] = 1
    l[b - 1][a - 1] = 1

g = [0 for _ in range(N)]
q = deque()

cnt = 0
for j in range(N):
    if g[j] == 0:
        q.append(j)
        while q:
            tmp = q.popleft()
            g[tmp] = 1
            for i in range(N):
                if l[tmp][i] == 1:
                    q.append(i)
                    l[tmp][i] = 0
                    g[i] = 1
        cnt += 1

print(cnt)

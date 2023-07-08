import sys
from collections import deque

read = sys.stdin.readline


def BFS():
    q = deque([1])
    par = [0 for _ in range(N + 1)]
    while q:
        tmp = q.popleft()
        for i in g[tmp]:
            if par[i] == 0 and i != 1:
                par[i] = tmp
                q.append(i)
    for i in range(2, N + 1):
        print(par[i])


N = int(read())

g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2 = map(int, read().split())
    g[n1].append(n2)
    g[n2].append(n1)

BFS()

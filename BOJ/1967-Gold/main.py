import sys

sys.setrecursionlimit(10**9)
read = sys.stdin.readline

n = int(read())
l = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, read().split())
    l[a].append((b, c))
    l[b].append((a, c))


def DFS(p, tmp):
    for b, c in l[p]:
        if dia[b] == -1:
            dia[b] = tmp + c
            DFS(b, tmp + c)


dia = [-1 for _ in range(n + 1)]
dia[1] = 0
DFS(1, 0)

init = dia.index(max(dia))
dia = [-1 for _ in range(n + 1)]
dia[init] = 0
DFS(init, 0)

print(max(dia))

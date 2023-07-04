import sys

read = sys.stdin.readline

n = int(read())
l = [[] for _ in range(n + 1)]
par = []

for _ in range(n - 1):
    a, b, c = map(int, read().split())
    par.append(a)
    l[a].append((b, c))

par = set(par)


def DFS(p, tmp, lr):
    length = len(l[p])
    if length >= 2:
        if tmp == 0:
            for i in range(length):
                DFS(l[p][i][0], tmp + l[p][i][1], i)
        else:
            for i in range(length):
                DFS(l[p][i][0], tmp + l[p][i][1], lr)
    elif len(l[p]) == 1:
        DFS(l[p][0][0], tmp + l[p][0][1], lr)
    elif len(l[p]) == 0:
        res[lr].append(tmp)


dia = []

for i in par:
    leng = len(l[i])
    if leng > 1:
        res = [[] for _ in range(leng)]
        DFS(i, 0, 0)
        resmax = [0 for _ in range(leng)]
        for i in range(leng):
            resmax[i] = max(res[i])
        resmax.sort(reverse=True)
        dia.append(resmax[0] + resmax[1])

print(max(dia))

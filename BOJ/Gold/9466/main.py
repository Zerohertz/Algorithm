import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(read())


def DFS(pos):
    global res
    visit[pos] = True
    tmp.append(pos)
    if visit[l[pos]]:
        if l[pos] in tmp:
            res += tmp[tmp.index(l[pos]):]
        return
    else:
        DFS(l[pos])


for _ in range(T):
    n = int(read())
    l = [0] + list(map(int, read().split()))
    visit = [False for _ in range(n + 1)]
    res = []
    for i in range(1, n + 1):
        if not visit[i]:
            tmp = []
            DFS(i)
    print(n - len(res))

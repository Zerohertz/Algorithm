import sys

read = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

K = int(read())


def DFS(pos, c):
    color[pos] = c
    for i in G[pos]:
        if color[i] == 0:
            status = DFS(i, -c)
            if not status:
                return False
        elif color[pos] == color[i]:
            return False
    return True


for _ in range(K):
    V, E = map(int, read().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, read().split())
        G[a].append(b)
        G[b].append(a)
    color = [0 for _ in range(V + 1)]
    for i in range(1, V + 1):
        if color[i] == 0:
            res = DFS(i, 1)
            if not res:
                break
    if res:
        print('YES')
    else:
        print('NO')

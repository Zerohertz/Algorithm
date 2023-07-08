import sys

read = sys.stdin.readline
N, M = map(int, read().split())
l = []


def DFS(start):
    if len(l) == M:
        print(" ".join(map(str, l)))
        return
    for i in range(start, N + 1):
        if not i in l:
            l.append(i)
            DFS(i + 1)
            l.pop()


DFS(1)

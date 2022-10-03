import sys

read = sys.stdin.readline

N, M = map(int, read().split())
lst = list(map(int, read().split()))
lst.sort()

l = []

def DFS():
    if len(l) == M:
        print(' '.join(list(map(str, l))))
        return
    else:
        for i in lst:
            if not i in l:
                l.append(i)
                DFS()
                l.pop()

DFS()
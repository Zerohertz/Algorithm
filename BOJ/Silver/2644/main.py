import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
a, b = map(int, read().split())
m = int(read())
l = [[] for _ in range(n + 1)]
for _ in range(m):
    c, d = map(int, read().split())
    l[c].append(d)
    l[d].append(c)


def BFS(start, end):
    q = deque([(start, 0)])
    visit = [False for _ in range(n + 1)]
    visit[start] = True
    while q:
        tmp, chon = q.popleft()
        for i in l[tmp]:
            if i == end:
                return chon + 1
            if not visit[i]:
                visit[i] = True
                q.append((i, chon + 1))
    return -1


print(BFS(a, b))

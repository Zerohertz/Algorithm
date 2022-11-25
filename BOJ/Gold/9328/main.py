import sys
from collections import deque

read = sys.stdin.readline

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]

def BFS(x, y):
    res = 0
    visit = [[False for _ in range(w + 2)] for _ in range(h + 2)]
    visit[x][y] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + v1[i], y + v2[i]
            if 0 <= nx < h + 2 and 0 <= ny < w + 2 and not visit[nx][ny]:
                if l[nx][ny] == '.':
                    visit[nx][ny] = True
                    q.append((nx, ny))
                elif l[nx][ny].islower():
                    door[ord(l[nx][ny]) - ord('a')] = True
                    visit = [[False for _ in range(w + 2)] for _ in range(h + 2)]
                    l[nx][ny] = '.'
                    q.append((nx, ny))
                elif l[nx][ny].isupper():
                    if door[ord(l[nx][ny]) - ord('A')]:
                        visit[nx][ny] = True
                        l[nx][ny] = '.'
                        q.append((nx, ny))
                elif l[nx][ny] == '$':
                    res += 1
                    visit[nx][ny] = True
                    l[nx][ny] = '.'
                    q.append((nx, ny))
    print(res)

T = int(read())

for _ in range(T):
    h, w = map(int, read().split())
    l = [list(read().rstrip()) for _ in range(h)]
    keys = list(read().strip())
    door = [False for _ in range(26)]
    for key in keys:
        if key != '0':
            door[ord(key) - ord('a')] = True
    for i in range(h):
        for j in range(w):
            if ord('A') <= ord(l[i][j]) <= ord('Z') and door[ord(l[i][j]) - ord('A')]:
                l[i][j] = '.'
    for i in l:
        i.insert(0, '.')
        i.append('.')
    l.insert(0, ['.'] * (w + 2))
    l.append(['.'] * (w + 2))
    BFS(0, 0)
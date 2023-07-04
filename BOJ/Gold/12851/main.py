import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

visit = [[-1, 0] for _ in range(100_001)]


def BFS(pos):
    q = deque([(pos, 0)])
    visit[pos][0] = 0
    visit[pos][1] = 1
    while q:
        tmp, t = q.popleft()
        for i in [tmp - 1, tmp + 1, tmp * 2]:
            if 0 <= i <= 100_000 and (
                    visit[i][0] == -1 or visit[i][0] == t + 1):
                if visit[i][0] == t + 1:
                    visit[i][1] += visit[tmp][1]
                else:
                    visit[i][0] = t + 1
                    visit[i][1] += visit[tmp][1]
                    q.append((i, t + 1))


BFS(N)
print(visit[K][0])
print(visit[K][1])

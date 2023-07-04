from collections import deque


def BFS(maps, start):
    visit = [False for _ in range(len(maps))]
    q = deque([start])
    visit[start] = True
    while q:
        tmp = q.popleft()
        for i in maps[tmp]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

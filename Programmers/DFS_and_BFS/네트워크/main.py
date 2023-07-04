from collections import deque


def BFS(computers, n, visit):
    q = deque()
    cnt = 0
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            q.append(i)
            cnt += 1
        while q:
            tmp = q.popleft()
            for j in range(n):
                if computers[tmp][j] == 1 and not visit[j]:
                    visit[j] = True
                    q.append(j)
    return cnt


def solution(n, computers):
    visit = [False for _ in range(n)]
    answer = BFS(computers, n, visit)
    return answer

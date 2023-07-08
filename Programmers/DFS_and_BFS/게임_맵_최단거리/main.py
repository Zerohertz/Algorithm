from collections import deque


def BFS(maps):
    v1 = [1, 0, -1, 0]
    v2 = [0, 1, 0, -1]
    q = deque([[0, 0]])
    N = len(maps)
    M = len(maps[0])
    maps[0][0] = 101
    while q:
        tmp = q.popleft()
        for i, j in zip(v1, v2):
            if (
                tmp[0] + i > -1
                and tmp[1] + j > -1
                and tmp[0] + i < N
                and tmp[1] + j < M
            ):
                if maps[tmp[0] + i][tmp[1] + j] == 1:
                    q.append([tmp[0] + i, tmp[1] + j])
                    maps[tmp[0] + i][tmp[1] + j] = maps[tmp[0]][tmp[1]] + 1
    return maps


def solution(maps):
    answer = BFS(maps)
    if answer[-1][-1] != 1:
        return answer[-1][-1] - 100
    else:
        return -1

def DFS(maps, pos, cnt):
    v1 = [1, 0, -1, 0]
    v2 = [0, 1, 0, -1]
    N = len(maps)
    M = len(maps[0])
    if pos[0] == N - 1 and pos[1] == M - 1:
        return maps
    else:
        for i, j in zip(v1, v2):
            if (
                pos[0] + i > -1
                and pos[1] + j > -1
                and pos[0] + i < N
                and pos[1] + j < M
            ):
                if maps[pos[0] + i][pos[1] + j] == 1:
                    cnt += 1
                    maps[pos[0] + i][pos[1] + j] = cnt
                    DFS(maps, [pos[0] + i, pos[1] + j], cnt)
    return maps


def solution(maps):
    maps[0][0] = 0
    answer = DFS(maps, [0, 0], 1)
    if answer[-1][-1] != 1:
        return answer[-1][-1]
    else:
        return -1

import sys
read = sys.stdin.readline

S = list(map(int, read().split()))
visited = [[False for _ in range(29)] for _ in range(29)]
visited[14][14] = 1

v1 = [1, -1, 0, 0]
v2 = [0, 0, -1, 1]


def DFS(x, y, pos, cnt):
    global res
    if cnt > 0:
        for i in range(4):
            nx, ny = x + v1[i], y + v2[i]
            if not visited[nx][ny]:
                visited[nx][ny] = True
                DFS(nx, ny, pos * S[i + 1] / 100, cnt - 1)
            else:
                continue
            visited[nx][ny] = False
    else:
        res += pos


res = 0
DFS(14, 14, 1, S[0])
print(res)
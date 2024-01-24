import sys

read = sys.stdin.readline


def preprocess(x, y, K, pos, tx, ty):
    if K == 1:
        return
    if not (x <= tx < x + 2**K and y <= ty < y + 2**K):
        if pos == 0:
            tx, ty = x + 2**K - 1, y + 2**K - 1
        elif pos == 1:
            tx, ty = x + 2**K - 1, y
        elif pos == 2:
            tx, ty = x, y + 2**K - 1
        elif pos == 3:
            tx, ty = x, y
        l[tx][ty] = -100
    preprocess(x, y, K - 1, 0, tx, ty)
    preprocess(x, y + 2 ** (K - 1), K - 1, 1, tx, ty)
    preprocess(x + 2 ** (K - 1), y, K - 1, 2, tx, ty)
    preprocess(x + 2 ** (K - 1), y + 2 ** (K - 1), K - 1, 3, tx, ty)


def BFS():
    global tmp
    visited = [[False for _ in range(2**K)] for _ in range(2**K)]
    for i in range(2**K):
        for j in range(2**K):
            if not visited[i][j]:
                visited[i][j] = True
                if l[i][j] == -100:
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if l[i + dx][j + dy] == -100:
                                l[i + dx][j + dy] = tmp
                                visited[i + dx][j + dy] = True
                    tmp += 1


def _tile(x, y, pos, tmp):
    cnt = 3
    dx = [range(x, x + 2), range(x + 1, x - 1, -1)]
    dy = [range(y, y + 2), range(y + 1, y - 1, -1)]
    for i in dx[pos // 2]:
        for j in dy[pos % 2]:
            if not l[i][j] and cnt:
                l[i][j] = tmp
                cnt -= 1


def tile(x, y, K, pos):
    global tmp
    if K <= 1:
        _tile(x, y, pos, tmp)
        tmp += 1
        return
    tile(x, y, K - 1, 0)
    tile(x, y + 2 ** (K - 1), K - 1, 1)
    tile(x + 2 ** (K - 1), y, K - 1, 2)
    tile(x + 2 ** (K - 1), y + 2 ** (K - 1), K - 1, 3)
    if K == 2:
        tile(x + 2**K // 4, y + 2**K // 4, K - 1, 0)


if __name__ == "__main__":
    K = int(read())
    x, y = map(int, read().split())
    l = [[0 for _ in range(2**K)] for _ in range(2**K)]
    tx, ty = 2**K - y, x - 1
    l[tx][ty] = -1
    tmp = 1
    preprocess(0, 0, K, 0, tx, ty)
    BFS()
    tile(0, 0, K, 0)
    for i in l:
        print("\t".join(map(str, i)))

"""
if not (2**K) ** 2 % 3 == 1:
    print(-1)
    exit()

>>> 2 ** (2 * 1) % 3
1
>>> 2 ** (2 * 2) % 3
1
>>> 2 ** (2 * 3) % 3
1
>>> 2 ** (2 * 4) % 3
1
>>> 2 ** (2 * 5) % 3
1
>>> 2 ** (2 * 6) % 3
1
>>> 2 ** (2 * 7) % 3
1
"""

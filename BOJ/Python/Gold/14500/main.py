import sys

read = sys.stdin.readline


def func1(map, x, y):
    try:
        return map[x][y] + map[x][y + 1] + map[x][y + 2] + map[x][y + 3]
    except:
        return 0


def func2(map, x, y):
    try:
        return map[x][y] + map[x][y + 1] + map[x + 1][y] + map[x + 1][y + 1]
    except:
        return 0


def func3(map, x, y):
    try:
        return map[x][y] + map[x + 1][y] + map[x + 2][y] + map[x + 2][y + 1]
    except:
        return 0


def func4(map, x, y):
    try:
        return map[x][y] + map[x + 1][y] + map[x + 1][y + 1] + map[x + 2][y + 1]
    except:
        return 0


def func5(map, x, y):
    try:
        return map[x][y] + map[x][y + 1] + map[x + 1][y + 1] + map[x][y + 2]
    except:
        return 0


def func6(map, x, y):
    try:
        return map[x][y] + map[x + 1][y] + map[x + 2][y] + map[x][y + 1]
    except:
        return 0


def func7(map, x, y):
    try:
        return map[x][y] + map[x][y + 1] + map[x + 1][y + 1] + map[x + 1][y + 2]
    except:
        return 0


if __name__ == "__main__":
    N, M = map(int, read().split())
    m1 = [[0 for _ in range(M)] for _ in range(N)]
    m2 = [[0 for _ in range(N)] for _ in range(M)]
    m3 = [[0 for _ in range(M)] for _ in range(N)]
    m4 = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(N):
        tmp = list(map(int, read().split()))
        for j in range(M):
            m1[i][j] = tmp[j]
            m2[j][N - i - 1] = m1[i][j]
            m3[N - i - 1][M - j - 1] = m1[i][j]
            m4[M - j - 1][i] = m1[i][j]

    res = 0
    for i in range(max(M, N)):
        for j in range(max(M, N)):
            res = max(
                res,
                func1(m1, i, j),
                func1(m2, i, j),
                func1(m3, i, j),
                func1(m4, i, j),
                func2(m1, i, j),
                func2(m2, i, j),
                func2(m3, i, j),
                func2(m4, i, j),
                func3(m1, i, j),
                func3(m2, i, j),
                func3(m3, i, j),
                func3(m4, i, j),
                func4(m1, i, j),
                func4(m2, i, j),
                func4(m3, i, j),
                func4(m4, i, j),
                func5(m1, i, j),
                func5(m2, i, j),
                func5(m3, i, j),
                func5(m4, i, j),
                func6(m1, i, j),
                func6(m2, i, j),
                func6(m3, i, j),
                func6(m4, i, j),
                func7(m1, i, j),
                func7(m2, i, j),
                func7(m3, i, j),
                func7(m4, i, j),
            )
    print(res)

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**9)

Di = (-1, 1, 0, 0)
Dj = (0, 0, -1, 1)


def panda(i, j):
    for di, dj in zip(Di, Dj):
        ni, nj = i + di, j + dj
        if not (0 <= ni < n and 0 <= nj < n):
            continue
        key, is_reversed = _get_key(i, j, ni, nj)
        if (_maps[key] == -1 and not is_reversed) or (_maps[key] == 1 and is_reversed):
            if 1 == cnts[ni][nj]:
                panda(ni, nj)
            cnts[i][j] = max(cnts[i][j], cnts[ni][nj] + 1)


def main():
    for i in range(n):
        for j in range(n):
            panda(i, j)
    return max([cnt for _cnts in cnts for cnt in _cnts])


def _get_key(i, j, ni, nj):
    if i < ni:
        return f"{i}-{j}-{ni}-{nj}", False
    if i > ni:
        return f"{ni}-{nj}-{i}-{j}", True
    if j < nj:
        return f"{i}-{j}-{ni}-{nj}", False
    if j > nj:
        return f"{ni}-{nj}-{i}-{j}", True
    return


if __name__ == "__main__":
    n = int(read())
    maps = [[] for _ in range(n)]
    for i in range(n):
        maps[i] = list(map(int, read().split()))
    """
    상, 하, 좌, 우
    -1 -> 이동 불가
    0 -> ==
    1 -> 이동 가능
    """
    _maps = {}
    for i in range(n):
        for j in range(n):
            for di, dj in zip(Di, Dj):
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < n):
                    continue
                key, is_reversed = _get_key(i, j, ni, nj)
                if key in _maps:
                    continue
                if maps[i][j] < maps[ni][nj]:
                    if is_reversed:
                        _maps[key] = -1
                    else:
                        _maps[key] = 1
                elif maps[i][j] > maps[ni][nj]:
                    if is_reversed:
                        _maps[key] = 1
                    else:
                        _maps[key] = -1
                else:
                    _maps[key] = 0
    cnts = [[1 for _ in range(n)] for _ in range(n)]
    print(main())

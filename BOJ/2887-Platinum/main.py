import heapq
import sys

read = sys.stdin.readline


def iter(from_, visited, candidates):
    for i in range(3):
        from__ = keys[i][from_]
        for j in [-1, 1]:
            to__ = from__
            while 0 <= to__ < N:
                to__ += j
                if 0 <= to__ < N:
                    to_ = maps[i][to__][1]
                    if not visited[to_]:
                        cost = abs(maps[i][from__][0] - maps[i][to__][0])
                        heapq.heappush(candidates, (cost, to_))
                        break


def mst():
    visited = [False for _ in range(N)]
    results = cnt = 0
    candidates = [(0, 0)]
    while cnt < N:
        cost, from_ = heapq.heappop(candidates)
        if visited[from_]:
            continue
        iter(from_, visited, candidates)
        results += cost
        visited[from_] = True
        cnt += 1
    print(results)


if __name__ == "__main__":
    N = int(read())
    maps = [[[] for _ in range(N)] for _ in range(3)]
    for i in range(N):
        x, y, z = map(int, read().split())
        maps[0][i] = (x, i)
        maps[1][i] = (y, i)
        maps[2][i] = (z, i)
    maps[0].sort(key=lambda x: x[0])
    maps[1].sort(key=lambda x: x[0])
    maps[2].sort(key=lambda x: x[0])
    keys = [[0 for _ in range(N)] for _ in range(3)]
    for idx, (x, y, z) in enumerate(zip(maps[0], maps[1], maps[2])):
        keys[0][x[1]] = idx
        keys[1][y[1]] = idx
        keys[2][z[1]] = idx
    mst()

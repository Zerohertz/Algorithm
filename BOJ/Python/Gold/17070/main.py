import sys

read = sys.stdin.readline


if __name__ == "__main__":
    N = int(read())
    Map = [[] for _ in range(N)]
    for i in range(N):
        Map[i] = list(map(int, read().split()))

    cnt = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
    cnt[0][1][0] = 1
    for i in range(2, N):
        if Map[0][i] == 0:
            cnt[0][i][0] = 1
        else:
            break
    for x in range(1, N):
        for y in range(1, N):
            if Map[x][y] == 0 and Map[x][y - 1] == 0 and Map[x - 1][y] == 0:
                cnt[x][y][2] = sum(cnt[x - 1][y - 1])
            if Map[x][y] == 0:
                cnt[x][y][0] = cnt[x][y - 1][0] + cnt[x][y - 1][2]
                cnt[x][y][1] = cnt[x - 1][y][1] + cnt[x - 1][y][2]
    print(sum(cnt[N - 1][N - 1]))

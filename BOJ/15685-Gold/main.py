import sys

read = sys.stdin.readline


DIRECTION = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def dragon():
    curve = [(0, 0)]
    for i in range(10):
        tmp = []
        for d, _ in curve[::-1]:
            td = (d + 2) % 4
            td = (td - 1) % 4
            tmp.append((td, i + 1))
        curve += tmp
    return curve


if __name__ == "__main__":
    N = int(read())
    grid = [[False for _ in range(101)] for _ in range(101)]
    DRAGON = dragon()
    for _ in range(N):
        x, y, d, g = map(int, read().split())
        grid[y][x] = True
        for d_, g_ in DRAGON:
            if g < g_:
                break
            d__ = (d + d_) % 4
            dy, dx = DIRECTION[d__]
            x += dx
            y += dy
            grid[y][x] = True
    cnt = 0
    for i in range(100):
        for j in range(100):
            if grid[i][j] and grid[i + 1][j] and grid[i][j + 1] and grid[i + 1][j + 1]:
                cnt += 1
    print(cnt)

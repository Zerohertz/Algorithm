import sys

read = sys.stdin.readline


def plane(x, y):
    n = max(abs(x), abs(y))
    nx, ny = n - x, n - y
    if x <= y:
        return (2 * n + 1) ** 2 - abs(nx) - abs(ny)
    else:
        return (2 * (n - 1) + 1) ** 2 + abs(nx) + abs(ny)


def abs2res(x, y):
    return y - r1, x - c1


if __name__ == "__main__":
    r1, c1, r2, c2 = map(int, read().split())
    results = [["" for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
    length = max(
        len(str(plane(c1, r1))),
        len(str(plane(c1, r2))),
        len(str(plane(c2, r2))),
        len(str(plane(c2, r1))),
    )
    for y in range(r1, r2 + 1):
        for x in range(c1, c2 + 1):
            ty, tx = abs2res(x, y)
            tmp = str(plane(x, y))
            results[ty][tx] = " " * (length - len(tmp)) + tmp
    for result in results:
        print(*result)

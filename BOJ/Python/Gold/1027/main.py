import sys

read = sys.stdin.readline


class Axis:
    def __init__(self, x1, y1, x2, y2):
        self.weight = (y2 - y1) / (x2 - x1)
        self.bias = y1 - self.weight * x1

    def __call__(self, x):
        return self.weight * x + self.bias


def brute(idx, dir):
    if dir == -1:
        iter = range(idx - 1, -1, -1)
    elif dir == 1:
        iter = range(idx + 1, N)
    axis = None
    cnt = 0
    for idx_ in iter:
        if not axis:
            axis = Axis(idx, buildings[idx], idx_, buildings[idx_])
            cnt += 1
            continue
        if buildings[idx_] > axis(idx_):
            axis = Axis(idx, buildings[idx], idx_, buildings[idx_])
            cnt += 1
    return cnt


def main():
    res = 0
    for idx in range(N):
        res = max(res, brute(idx, -1) + brute(idx, 1))
    return res


if __name__ == "__main__":
    N = int(read())
    buildings = list(map(int, read().split()))
    print(main())

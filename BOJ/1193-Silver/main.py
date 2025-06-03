import math
import sys


def solution(X):
    if X == 1:
        print("1/1")
    else:
        est_n = int(math.sqrt(2 * X))
        if est_n * (est_n - 1) < 2 * X <= est_n * (est_n + 1):
            n = est_n
        else:
            est_n += 1
            n = est_n
        m = n * (n + 1) // 2
        if n % 2 == 0:
            x, y = n, 1
            x -= m - X
            y += m - X
        else:
            x, y = 1, n
            x += m - X
            y -= m - X
        print(str(x) + "/" + str(y))


if __name__ == "__main__":
    read = sys.stdin.readline
    X = int(read())
    solution(X)

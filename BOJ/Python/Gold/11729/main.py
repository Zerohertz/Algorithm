import sys

read = sys.stdin.readline


def move(n, start, end):
    if n == 1:
        print(start, end)
        return

    move(n - 1, start, 6 - start - end)
    print(start, end)
    move(n - 1, 6 - start - end, end)


if __name__ == "__main__":
    N = int(read())
    print(2**N - 1)
    move(N, 1, 3)

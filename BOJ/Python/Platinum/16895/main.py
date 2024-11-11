import sys

read = sys.stdin.readline


def main():
    grundy = 0
    for pi in P:
        grundy ^= pi
    if not grundy:
        return 0
    if N == 1:
        return 1
    cnt = 0
    for pi in P:
        if pi ^ grundy <= pi:
            cnt += 1
    return cnt


if __name__ == "__main__":
    N = int(read())
    P = list(map(int, read().split()))
    print(main())

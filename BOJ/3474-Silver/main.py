import sys

read = sys.stdin.readline


if __name__ == "__main__":
    T = int(read())
    L = [5**i for i in range(1, 20)]
    for _ in range(T):
        N = int(read())
        res = 0
        for l in L:
            res += N // l
        print(res)

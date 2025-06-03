import sys

read = sys.stdin.readline


def main():
    grundy = 0
    for pi in P:
        grundy ^= pi
    if grundy:
        print(PLAYERS[0])
    else:
        print(PLAYERS[1])


if __name__ == "__main__":
    PLAYERS = ["koosaga", "cubelover"]
    N = int(read())
    P = list(map(int, read().split()))
    main()

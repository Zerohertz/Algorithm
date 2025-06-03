import sys

read = sys.stdin.readline


def main():
    grundy = 0
    for pi in P:
        grundy ^= pi
    if all(pi <= 1 for pi in P):
        if len(P) % 2 == 1:
            return PLAYERS[1]
        return PLAYERS[0]
    if not grundy:
        return PLAYERS[1]
    return PLAYERS[0]


if __name__ == "__main__":
    PLAYERS = ["koosaga", "cubelover"]
    N = int(read())
    P = list(map(int, read().split()))
    print(main())

import sys
from itertools import product

read = sys.stdin.readline

"""
def recurse(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return recurse(20, 20, 20)
    if a < b and b < c:
        return recurse(a, b, c - 1) + recurse(a, b - 1, c - 1) - recurse(a, b - 1, c)
    return (
        recurse(a - 1, b, c)
        + recurse(a - 1, b - 1, c)
        + recurse(a - 1, b, c - 1)
        - recurse(a - 1, b - 1, c - 1)
    )

while True:
    a, b, c = map(int, read().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {recurse(a, b, c)}")
"""

if __name__ == "__main__":
    dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    iters = list(product(range(1, 21), repeat=3))
    for c, b, a in iters:
        if a < b and b < c:
            dp[a][b][c] = dp[a][b][c - 1] + dp[a][b - 1][c - 1] - dp[a][b - 1][c]
        else:
            dp[a][b][c] = (
                dp[a - 1][b][c]
                + dp[a - 1][b - 1][c]
                + dp[a - 1][b][c - 1]
                - dp[a - 1][b - 1][c - 1]
            )
    while True:
        a, b, c = map(int, read().split())
        if a == -1 and b == -1 and c == -1:
            break
        na, nb, nc = a, b, c
        if na <= 0 or nb <= 0 or nc <= 0:
            print(f"w({a}, {b}, {c}) = 1")
            continue
        if na > 20 or nb > 20 or nc > 20:
            na = nb = nc = 20
        print(f"w({a}, {b}, {c}) = {dp[na][nb][nc]}")

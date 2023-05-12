import sys


def find_par(x):
    if par[x] != x:
        par[x] = find_par(par[x])
    return par[x]

def union(b, c):
    b, c = find_par(b), find_par(c)
    if b < c:
        par[c] = b
    else:
        par[b] = c

if __name__ == "__main__":
    sys.setrecursionlimit(1_000_000_000)
    read = sys.stdin.readline
    n, m = map(int, read().split())
    par = [i for i in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, read().split())
        if a == 0:
            union(b, c)
        else:
            if find_par(b) == find_par(c):
                print('YES')
            else:
                print('NO')
import sys

read = sys.stdin.readline

T = int(read())
for _ in range(T):
    n = int(read())
    l = [[0 for _ in range(n + 1)] for _ in range(2)]
    d = [[0 for _ in range(n + 1)] for _ in range(2)]
    for i in range(2):
        l[i] = [0] + list(map(int, read().split()))
    d[0][0], d[1][0] = 0, 0
    d[0][1], d[1][1] = l[0][1], l[1][1]
    for i in range(2, n + 1):
        d[0][i] = max(d[1][i - 2], d[1][i - 1]) + l[0][i]
        d[1][i] = max(d[0][i - 2], d[0][i - 1]) + l[1][i]
    print(max(max(d[0][-2:]), max(d[1][-2:])))

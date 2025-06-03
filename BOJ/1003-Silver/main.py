import sys

read = sys.stdin.readline

T = int(read())
l = [[0, 0] for _ in range(41)]

for i in range(41):
    if i == 0:
        l[i] = [1, 0]
    elif i == 1:
        l[i] = [0, 1]
    else:
        l[i] = [l[i - 2][0] + l[i - 1][0], l[i - 2][1] + l[i - 1][1]]

for _ in range(T):
    N = int(read())
    print(l[N][0], l[N][1])

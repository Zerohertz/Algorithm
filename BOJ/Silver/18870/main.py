import sys

read = sys.stdin.readline

N = int(read())
l1 = list(map(int, read().split()))
l2 = [[l1[i], i] for i in range(N)]
l2.sort(key=lambda x: x[0])
l3 = [0 for _ in range(N)]
tmp, reg = 0, -10**10
for i in range(N):
    if i == 0:
        l3[l2[i][1]] = tmp
    else:
        if l2[i - 1][0] == l2[i][0]:
            l3[l2[i][1]] = tmp
        else:
            tmp += 1
            l3[l2[i][1]] = tmp
for i in l3:
    print(i, end=' ')

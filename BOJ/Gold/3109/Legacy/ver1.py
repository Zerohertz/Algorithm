import sys

read = sys.stdin.readline

R, C = map(int, read().split())

l = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    l[i] = list(read().rstrip())

cnt = 0
for i in range(R):
    dict = {}
    j = 0
    ii = 0
    while j < C - 1:
        if l[i + ii][j + 1] == '.':
            dict[j + 1] = i + ii
            # l[i + ii][j + 1] = 'x'
        elif i + ii + 1 < R and l[i + ii + 1][j + 1] == '.':
            dict[j + 1] = i + ii + 1
            # l[i + ii + 1][j + 1] = 'x'
            ii += 1
        elif i + ii - 1 >= 0 and l[i + ii - 1][j + 1] == '.':
            dict[j + 1] = i + ii - 1
            # l[i + ii - 1][j + 1] = 'x'
            ii -= 1
        else:
            cnt -= 1
            break
        j += 1
        if j >= C - 1:
            for k in range(1, C):
                print(k)
                l[dict[k]][k] = 'x'
    cnt += 1

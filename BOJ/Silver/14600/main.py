import sys

read = sys.stdin.readline


def tile(x, y, K, pos):
    global tmp
    if K <= 1:
        cnt = 3
        if pos == 0 or pos == 4:
            for i in range(x, x + 2):
                for j in range(y, y + 2):
                    if not l[i][j] and cnt:
                        l[i][j] = tmp
                        cnt -= 1
        elif pos == 1:
            for i in range(x, x + 2):
                for j in range(y + 1, y - 1, -1):
                    if not l[i][j] and cnt:
                        l[i][j] = tmp
                        cnt -= 1
        elif pos == 2:
            for i in range(x + 1, x - 1, -1):
                for j in range(y, y + 2):
                    if not l[i][j] and cnt:
                        l[i][j] = tmp
                        cnt -= 1
        elif pos == 3:
            for i in range(x + 1, x - 1, -1):
                for j in range(y + 1, y - 1, -1):
                    if not l[i][j] and cnt:
                        l[i][j] = tmp
                        cnt -= 1
        tmp += 1
        return
    tile(x, y, K - 1, 0)
    tile(x, y + 2**(K - 1), K - 1, 1)
    tile(x + 2**(K - 1), y, K - 1, 2)
    tile(x + 2**(K - 1), y + 2**(K - 1), K - 1, 3)
    tile(x + 2**K // 4, y + 2**K // 4, K - 1, 4)


K = int(read())
x, y = map(int, read().split())

l = [[0 for _ in range(2**K)] for _ in range(2**K)]
l[2**K - y][x - 1] = -1

tmp = 1
tile(0, 0, K, 0)

for i in l:
    for j in i:
        print(j, end=' ')
    print()

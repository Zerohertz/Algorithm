import sys

read = sys.stdin.readline

M = int(read())
tmp = 0
xor = 0

for _ in range(M):
    l = list(map(int, read().split()))
    if l[0] == 1:
        tmp += l[1]
        xor ^= l[1]
    elif l[0] == 2:
        tmp -= l[1]
        xor ^= l[1]
    elif l[0] == 3:
        print(tmp)
    elif l[0] == 4:
        print(xor)

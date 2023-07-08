import sys

read = sys.stdin.readline

N = int(read())
l = sorted(map(int, read().split()))

tmp = 1
for i in l:
    if tmp < i:
        break
    tmp += i

print(tmp)

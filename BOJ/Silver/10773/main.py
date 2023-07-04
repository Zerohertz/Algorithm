import sys

read = sys.stdin.readline

N = int(read())
l = []
for i in range(N):
    tmp = int(read())
    if tmp == 0:
        l.pop()
    else:
        l.append(tmp)

print(sum(l))

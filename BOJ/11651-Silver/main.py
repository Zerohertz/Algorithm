import sys

read = sys.stdin.readline

N = int(read())
l = []
for i in range(N):
    l.append(list(map(int, read().split())))

l.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(l[i][0], l[i][1])

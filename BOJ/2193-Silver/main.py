import sys

read = sys.stdin.readline

N = int(read())

l = [0 for _ in range(91)]
l[1] = 1
l[2] = 1
l[3] = 2
for i in range(3, N + 1):
    l[i] = l[i - 1] + l[i - 2]

print(l[N])

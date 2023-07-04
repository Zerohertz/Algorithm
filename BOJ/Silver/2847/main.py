import sys

read = sys.stdin.readline

N = int(read())
l = []
for _ in range(N):
    l.append(int(read()))

res = 0
for i in range(N - 1, 0, -1):
    if l[i] <= l[i - 1]:
        res += l[i - 1] - l[i] + 1
        l[i - 1] = l[i] - 1

print(res)

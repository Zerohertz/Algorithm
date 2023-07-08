import sys

read = sys.stdin.readline

N = int(read())
l = sorted(map(int, read().split()))

res = 0
for i in range(N):
    res += sum(l[0: i + 1])

print(res)

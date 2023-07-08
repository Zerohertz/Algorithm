import sys

read = sys.stdin.readline

N = int(read())
l = [0 for _ in range(N + 1)]
for i in range(2, N + 1):
    l[i] = l[i - 1] + 1
    if i % 3 == 0:
        l[i] = min(l[i], l[i // 3] + 1)
    if i % 2 == 0:
        l[i] = min(l[i], l[i // 2] + 1)

print(l[N])

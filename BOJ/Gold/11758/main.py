import sys

read = sys.stdin.readline

x = [0 for _ in range(3)]
y = [0 for _ in range(3)]

for i in range(3):
    x[i], y[i] = map(int, read().split())

tmp = 0
tmp += x[0] * y[1] - x[1] * y[0]
tmp += x[1] * y[2] - x[2] * y[1]
tmp += x[2] * y[0] - x[0] * y[2]

if tmp == 0:
    print(0)
elif tmp > 0:
    print(1)
else:
    print(-1)

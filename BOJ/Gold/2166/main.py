import sys
read = sys.stdin.readline

N = int(read())
x = [0 for _ in range(N)]
y = [0 for _ in range(N)]
for i in range(N):
  x[i], y[i] = map(int, read().split())

x.append(x[0])
y.append(y[0])

xr, yr = 0, 0

for i in range(N):
  xr += x[i] * y[i + 1]
  yr += y[i] * x[i + 1]

print(round(1 / 2 * abs(xr - yr), 1))
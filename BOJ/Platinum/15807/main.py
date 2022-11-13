import sys
read = sys.stdin.readline

N = int(read())
light = [[0 for _ in range(3002)] for _ in range(3002)]
for i in range(N):
  x, y = map(int, read().split())
  light[x + 1501][y + 1501] += 1

axis = [[0 for _ in range(3002)] for _ in range(3002)]
diag1 = [0 for _ in range(6004)]
diag2 = [0 for _ in range(6004)]

for y in range(1, 3002):
  for x in range(1, 3002):
    axis[x][y] = diag1[3002 + x - y] + axis[x][y - 1] + diag2[x + y] + light[x][y]
    diag1[3002 + x - y] += light[x][y]
    diag2[x + y] += light[x][y]

P = int(read())
for i in range(P):
  x, y = map(int, read().split())
  print(axis[x + 1501][y + 1501])
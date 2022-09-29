import sys
read = sys.stdin.readline

n = int(read())
l = []
for i in range(n):
  l.append(list(map(int, read().split())))

for i in range(1, n):
  for j in range(i + 1):
    if 0 == j:
      l[i][j] += l[i - 1][0]
    elif j == i:
      l[i][j] += l[i - 1][j - 1]
    else:
      l[i][j] += max(l[i - 1][j - 1], l[i - 1][j])

print(max(l[n - 1]))
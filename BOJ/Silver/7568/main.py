import sys
read = sys.stdin.readline

N = int(read())
l = []
for i in range(N):
  l.append(list(map(int, read().split())))

res = []
for i in range(N):
  cnt = 0
  for j in range(N):
    if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
      cnt += 1
  res.append(cnt + 1)

for i in res:
  print(i, end = ' ')
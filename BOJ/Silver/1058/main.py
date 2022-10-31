import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
g = [[] for _ in range(N)]

for i in range(N):
  s = read().rstrip()
  for j, k in enumerate(s):
    if k == 'Y':
      g[i].append(j)

def friend(start):
  f = 0
  q = deque([(start, 0)])
  v = [False for _ in range(N)]
  v[start] = True
  while q:
    tmp = q.popleft()
    for i in g[tmp[0]]:
      if tmp[1] < 2 and not v[i]:
        v[i] = True
        q.append((i, tmp[1] + 1))
        f += 1
  return f

res = 0
for i in range(N):
  res = max(res, friend(i))

print(res)
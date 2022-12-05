import sys
from itertools import combinations
N = int(sys.stdin.readline())

l = [str(i) for i in range(10)]
res = []

for i in range(1, 10):
  for j in combinations(l, i):
    res.append(int(''.join(j[::-1])))

res.sort()
res.append(9876543210)

if N - 1 < len(res):
  print(res[N - 1])
else:
  print(-1)
import sys
from collections import Counter
read = sys.stdin.readline

N = int(read())
l = [[] for _ in range(8)]

for i in range(N):
  tmp = read().rstrip()
  idx = 0
  for j in tmp[::-1]:
    l[idx].append(j)
    idx += 1

C = []
for i in l:
  C.append(Counter(i))

d = {}
tmp = 9
for i in C[::-1]:
  for j in i:
    if not j in d:
      d[j] = tmp
      tmp -= 1

res = 0
for i, j in enumerate(l):
  for k in j:
    res += 10 ** i * d[k]

print(res)
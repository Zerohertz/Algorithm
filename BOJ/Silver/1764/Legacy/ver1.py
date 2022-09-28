import sys
read = sys.stdin.readline

N, M = map(int, read().split())

l1 = []
l2 = []

for _ in range(N):
  l1.append(read().rstrip())

for _ in range(M):
  l2.append(read().rstrip())

res = 0
l3 = []
for i in range(M):
  if l2[i] in l1:
    res += 1
    l3.append(l2[i])

l3.sort()
print(res)
for i in range(res):
  print(l3[i])
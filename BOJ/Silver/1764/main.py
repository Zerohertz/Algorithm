import sys
read = sys.stdin.readline

N, M = map(int, read().split())

l1 = set()
l2 = set()

for _ in range(N):
  l1.add(read().rstrip())

for _ in range(M):
  l2.add(read().rstrip())

res = sorted(list(l1 & l2))

print(len(res))
for i in res:
  print(i)
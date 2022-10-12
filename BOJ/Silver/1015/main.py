import sys
read = sys.stdin.readline

N = int(read())
A = list(map(int, read().split()))
a = [i for i in A]
a.sort()
P = []
for i in A:
  P.append(a.index(i))
  a[a.index(i)] = -100

for res in P:
  print(res, end = " ")
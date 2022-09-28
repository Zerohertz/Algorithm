import sys
read = sys.stdin.readline

T = int(read())
l = [0 for _ in range(11)]
l[1] = 1
l[2] = 2
l[3] = 4
for i in range(4, 11):
  l[i] = l[i-3] + l[i-2] + l[i-1]

for i in range(T):
  tmp = int(read())
  print(l[tmp])
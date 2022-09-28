import sys
read = sys.stdin.readline

n = int(read())
l = [0 for _ in range(1001)]
l[1] = 1
l[2] = 2
if n > 2:
  for i in range(3, 1001):
    l[i] = l[i-2] + l[i-1]

print(l[n] % 10_007)
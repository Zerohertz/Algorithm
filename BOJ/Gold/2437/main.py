import sys
read = sys.stdin.readline

N = int(read())
l = list(map(int, read().split()))
l.sort()

tmp = 1
for i in l:
  if tmp < i:
    break
  tmp += i

print(tmp)
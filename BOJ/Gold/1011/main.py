import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
  a, b = map(int, read().split())
  tmp = b - a
  max = int(tmp ** 0.5)
  tmp -= max ** 2
  cnt = 2 * max - 1
  if tmp % max == 0:
    cnt += tmp // max
  else:
    cnt += tmp // max + 1
  print(cnt)
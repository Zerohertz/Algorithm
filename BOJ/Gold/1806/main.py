import sys
read = sys.stdin.readline

N, S = map(int, read().split())
l = list(map(int, read().split()))

idx1 = 0
idx2 = 0
tmp = 0
res = sys.maxsize

while True:
  if S <= tmp:
    res = min(res, idx2 - idx1)
    tmp -= l[idx1]
    idx1 += 1
  elif S > tmp:
    idx2 += 1
    if N < idx2:
      break
    tmp += l[idx2 - 1]
  if idx1 > idx2:
    idx2 += 1
    tmp += l[idx2 - 1]

if res == sys.maxsize:
  print(0)
else:
  print(res)
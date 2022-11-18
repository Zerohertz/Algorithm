import sys
read = sys.stdin.readline

N = int(read())
l = list(map(int, read().split()))
l.sort()

res = [0, 0, 0]
liquid = sys.maxsize

for idx3 in range(0, N - 2):
  idx1 = idx3 + 1
  idx2 = N - 1
  while True:
    tmp = l[idx1] + l[idx2] + l[idx3]
    if liquid >= abs(tmp):
      liquid = abs(tmp)
      res = [idx1, idx2, idx3]
    if tmp < 0:
      idx1 += 1
    elif tmp > 0:
      idx2 -= 1
    else:
      break
    if idx1 >= idx2:
      break

print(l[res[2]], l[res[0]], l[res[1]])
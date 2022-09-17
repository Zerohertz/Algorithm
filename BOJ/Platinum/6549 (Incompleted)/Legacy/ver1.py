import sys
read = sys.stdin.readline

def returnSize(L, tar):
  st = 0
  for i in range(tar):
    if L[tar - i - 1] >= L[tar]:
      st += 1
    else:
      break
  for i in range(tar + 1, len(L)):
    if L[i] >= L[tar]:
      st += 1
    else:
      break
  return (st + 1) * L[tar]

while 1:
  L = list(map(int,read().split()))
  sc = []
  if L[0] == 0 and len(L) == 1:
    break
  del L[0]
  for i in range(len(L)):
    sc.append(returnSize(L, i))
  print(max(sc))
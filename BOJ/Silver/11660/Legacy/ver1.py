import sys
read = sys.stdin.readline

def cal(tar):
  res = 0
  for i in range(tar[0] - 1, tar[2]):
    for j in range(tar[1] - 1, tar[3]):
      res += l[i][j]
  return res

N, M = map(int, read().split())
l = [[] for _ in range(N)]

for i in range(N):
  l[i] = list(map(int, read().split()))

c = [[] for _ in range(M)]

for i in range(M):
  c[i] = list(map(int, read().split()))

for i in range(M):
  print(cal(c[i]))
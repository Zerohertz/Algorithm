N, M = map(int, input().split())

d1 = dict()
d2 = dict()
for i in range(N):
  tmp = input()
  d1[i + 1] = tmp
  d2[tmp] = i + 1

for i in range(M):
  tmp = input()
  try:
    tmp = int(tmp)
    print(d1[tmp])
  except:
    print(d2[tmp])
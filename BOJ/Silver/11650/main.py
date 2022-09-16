N = int(input())

L = []

for i in range(N):
  a,b = map(int, input().split())
  L.append([a, b])

L.sort(key = lambda x: (x[0], x[1]))

for i in range(N):
  print(L[i][0], L[i][1])
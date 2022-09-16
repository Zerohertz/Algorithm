N = int(input())
L = []
for _ in range(N):
  a,b = input().split()
  L.append([int(a),b])

L.sort(key = lambda x: (x[0]))

for i in range(N):
  print(L[i][0], L[i][1])
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in range(M):
  tmp = 0
  for j in range(N):
    if B[i] == A[j]:
      tmp += 1
  if tmp == 0:
    print(0)
  else:
    print(1)
import math

T = int(input())

N = []
M = []

for i in range(T):
  a,b = input().split()
  N.append(int(a))
  M.append(int(b))

for i in range(T):
  print(int(math.factorial(M[i])/(math.factorial(M[i]-N[i])*math.factorial(N[i]))))
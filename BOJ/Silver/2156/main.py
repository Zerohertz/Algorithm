import sys
read = sys.stdin.readline

N = int(read())
L = [0] + [int(read()) for _ in range(N)] + [0]
P = [0] * (N+2)
P[1] = L[1]
P[2] = P[1] + L[2]

for i in range(3, N+1):
  P[i] = max(P[i-3]+L[i-1]+L[i], P[i-2]+L[i], P[i-1])

print(P[N])
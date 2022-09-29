import sys
read = sys.stdin.readline

N, K = map(int, read().split())
A = [0 for _ in range(N)]

for i in range(N):
  A[i] = int(read())

A = A[::-1]

cnt = 0
for i in A:
  tmpcnt = K // i
  cnt += tmpcnt
  K -= i * tmpcnt

print(cnt)
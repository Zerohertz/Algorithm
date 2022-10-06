import sys
read = sys.stdin.readline

N, M = map(int, read().split())

if N > 2:
  if M <= 6:
    print(min(4, M))
  else:
    print(M - 2)
else:
  if N == 2:
    print(min(4, (M + 1) // 2))
  else:
    print(1)
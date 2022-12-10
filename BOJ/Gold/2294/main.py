import sys
read = sys.stdin.readline

n, k = map(int, read().split())

l = []
dp = [sys.maxsize for _ in range(10_001)]
for i in range(n):
  tmp = int(read())
  if tmp <= 10_000:
    l.append(tmp)
    dp[tmp] = 1

for i in range(1, 10_001):
  for j in l:
    if i + j < 10_001:
      dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[k] == sys.maxsize:
  print(-1)
else:
  print(dp[k])
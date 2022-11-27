import sys
read = sys.stdin.readline

N = int(read())

dp1 = [0 for _ in range(3)]
dp2 = [0 for _ in range(3)]
tmp1 = [0 for _ in range(3)]
tmp2 = [0 for _ in range(3)]

for i in range(N):
  a, b, c = map(int, read().split())
  for j in range(3):
    if j == 0:
      tmp1[j] = a + max(dp1[j], dp1[j + 1])
      tmp2[j] = a + min(dp2[j], dp2[j + 1])
    elif j == 1:
      tmp1[j] = b + max(dp1[j - 1], dp1[j], dp1[j + 1])
      tmp2[j] = b + min(dp2[j - 1], dp2[j], dp2[j + 1])
    elif j == 2:
      tmp1[j] = c + max(dp1[j - 1], dp1[j])
      tmp2[j] = c + min(dp2[j - 1], dp2[j])
  for j in range(3):
    dp1[j] = tmp1[j]
    dp2[j] = tmp2[j]

print(max(dp1), min(dp2))
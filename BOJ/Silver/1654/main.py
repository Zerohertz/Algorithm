def countLan(l, length):
  res = 0
  for i in range(len(l)):
    res += l[i] // length
  return res

K, N = map(int, input().split())

l = [0 for i in range(K)]
for i in range(K):
  l[i] = int(input())

m = 1
M = max(l)
ans = 0

while (m <= M):
  mid = int((m + M) / 2)
  if countLan(l, mid) >= N:
    m = mid + 1
    if ans < mid:
      ans = mid
  else:
    M = mid - 1

print(ans)
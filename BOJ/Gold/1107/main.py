import sys
read = sys.stdin.readline

N = int(read())
M = int(read())

l = []
if M != 0:
  l = list(map(int, read().split()))

res = abs(N - 100)

for i in range(1000001):
  stri = str(i)
  for j in range(len(stri)):
    if int(stri[j]) in l:
      break
    elif j == len(stri) - 1:
      res = min(res, len(stri) + abs(N - int(stri)))

print(res)
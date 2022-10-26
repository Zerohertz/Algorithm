N = int(input())

res = 0
r = [0 for _ in range(N)]

def is_promising(x):
  for i in range(x):
    if r[x] == r[i] or abs(r[x] - r[i]) == abs(x - i):
      return False
  return True

def n_queens(x):
  global res
  if x == N:
    res += 1
    return
  else:
    for i in range(N):
      r[x] = i
      if is_promising(x):
        n_queens(x + 1)

n_queens(0)
print(res)
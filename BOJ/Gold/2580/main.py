import sys
read = sys.stdin.readline

l = [[0 for _ in range(9)] for _ in range(9)]
target = []
for i in range(9):
  l[i] = list(map(int, read().split()))
  for j in range(9):
    if l[i][j] == 0:
      target.append((i, j))

def row(x, a):
  for i in range(9):
    if a == l[x][i]:
      return False
  return True

def col(y, a):
  for i in range(9):
    if a == l[i][y]:
      return False
  return True

def box(x, y, a):
  x = x // 3 * 3
  y = y // 3 * 3
  for i in range(3):
    for j in range(3):
      if a == l[x + i][y + j]:
        return False
  return True

def DFS(idx):
  if len(target) == idx:
    for i in range(9):
      print(*l[i])
    exit()
  x, y = target[idx]
  for i in range(1, 10):
    if row(x, i) and col(y, i) and box(x, y, i):
      l[x][y] = i
      DFS(idx + 1)
      l[x][y] = 0

DFS(0)
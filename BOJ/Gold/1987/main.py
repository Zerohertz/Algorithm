import sys
read = sys.stdin.readline

R, C = map(int, read().split())
l = [['' for _ in range(C)] for _ in range(R)]
for i in range(R):
  l[i] = list(read().rstrip())

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]
alphabet = [False for _ in range(26)]
res = 0

def DFS(pos, cnt):
  global res
  res = max(cnt, res)
  x, y = pos
  for a, b in zip(v1, v2):
    nx, ny = x + a, y + b
    if 0 <= nx < R and 0 <= ny < C:
      if not alphabet[ord(l[nx][ny]) - ord('A')]:
        alphabet[ord(l[nx][ny]) - ord('A')] = True
        DFS((nx, ny), cnt + 1)
        alphabet[ord(l[nx][ny]) - ord('A')] = False

alphabet[ord(l[0][0]) - ord('A')] = True
DFS((0, 0), 1)
print(res)
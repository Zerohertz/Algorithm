import sys
read = sys.stdin.readline

R, C = map(int, read().split())
l = [list(read().rstrip()) for _ in range(R)]

v1 = [1, 0, -1, 0]
v2 = [0, 1, 0, -1]
alphabet = [0 for _ in range(26)]
res = 0

def DFS(x, y, cnt):
  global res
  res = max(cnt, res)
  for i in range(4):
    nx, ny = x + v1[i], y + v2[i]
    if 0 <= nx < R and 0 <= ny < C and alphabet[ord(l[nx][ny]) - 65] == 0:
      alphabet[ord(l[nx][ny]) - 65] = 1
      DFS(nx, ny, cnt + 1)
      alphabet[ord(l[nx][ny]) - 65] = 0

alphabet[ord(l[0][0]) - 65] = 1
DFS(0, 0, 1)
print(res)
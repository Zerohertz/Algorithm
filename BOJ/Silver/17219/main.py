import sys
read = sys.stdin.readline

N, M = map(int, read().split())
d = {}

for _ in range(N):
  site, pwd = map(str, read().rstrip().split())
  d[site] = pwd

for _ in range(M):
  site = read().rstrip()
  print(d[site])
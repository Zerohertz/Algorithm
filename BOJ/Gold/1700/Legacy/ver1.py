import sys
from collections import deque
read = sys.stdin.readline

N, K = map(int, read().split())
l = list(map(int, read().split()))

cnt = 0
q = deque()

if N >= len(set(l)):
  print(0)
else:
  for i, j in enumerate(l):
    if not j in q:
      if len(q) >= N:
        idx = -1
        tmp = l[i:]
        for k in q:
          if k in tmp:
            tar = tmp.index(k)
            if idx < tar:
              idx = tar
              val = k
          else:
            val = k
            break
        q.remove(val)
        cnt += 1
        q.append(j)
      else:
        q.append(j)

print(cnt)
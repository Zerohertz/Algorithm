import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

q = deque([N])
lt = [-1 for _ in range(100_001)]
lt[N] = 0
while q:
    tmp = q.popleft()
    if tmp == K:
        break
    if 2 * tmp <= 100_000 and lt[2 * tmp] == -1:
        lt[2 * tmp] = lt[tmp]
        q.appendleft(2 * tmp)
    if tmp - 1 >= 0 and tmp - 1 <= 100_000 and lt[tmp - 1] == -1:
        lt[tmp - 1] = lt[tmp] + 1
        q.append(tmp - 1)
    if tmp + 1 >= 0 and tmp + 1 <= 100_000 and lt[tmp + 1] == -1:
        lt[tmp + 1] = lt[tmp] + 1
        q.append(tmp + 1)

print(lt[K])

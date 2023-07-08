import sys
from collections import deque

read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N = int(read())
    q = deque(list(map(str, read().split())))
    if N == 1:
        print(q[0])
    else:
        S = q.popleft()
        tmp = q.popleft()
        if ord(S) <= ord(tmp):
            S += tmp
        else:
            S = tmp + S
        for _ in range(N - 2):
            tmp = q.popleft()
            if ord(S[0]) >= ord(tmp):
                S = tmp + S
            else:
                S += tmp
        print(S)

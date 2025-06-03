import sys
from collections import deque

read = sys.stdin.readline

T = int(read())
for _ in range(T):
    k = int(read())
    Q = deque()
    for _ in range(k):
        a, b = read().split()
        b = int(b)
        if a == "I":
            Q.append(b)
        elif a == "D":
            if Q:
                if b == -1:
                    tmp = min(Q)
                    Q.remove(tmp)
                elif b == 1:
                    tmp = max(Q)
                    Q.remove(tmp)
    if Q:
        print(max(Q), min(Q))
    else:
        print("EMPTY")

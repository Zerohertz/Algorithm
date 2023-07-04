import sys
from collections import deque

read = sys.stdin.readline


def comm(s):
    if 'push' == s[0]:
        q.append(int(s[1]))
    elif 'pop' == s[0]:
        try:
            print(q.popleft())
        except BaseException:
            print(-1)
    elif 'size' == s[0]:
        print(len(q))
    elif 'empty' == s[0]:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif 'front' == s[0]:
        try:
            print(q[0])
        except BaseException:
            print(-1)
    elif 'back' == s[0]:
        try:
            print(q[-1])
        except BaseException:
            print(-1)


if __name__ == "__main__":
    q = deque([])
    N = int(read())
    for _ in range(N):
        s = read().strip().split()
        comm(s)

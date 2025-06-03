import sys
from collections import deque

read = sys.stdin.readline

if __name__ == "__main__":
    N = int(read())
    top = list(map(int, read().split()))
    res = [0 for _ in range(N)]
    stack = deque()
    for i in range(N):
        while stack:
            if stack[-1][1] < top[i]:
                stack.pop()
            else:
                res[i] = stack[-1][0] + 1
                break
        stack.append((i, top[i]))
    print(*res)

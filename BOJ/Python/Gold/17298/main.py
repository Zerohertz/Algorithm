import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N = int(read())
    A = list(map(int, read().split()))
    NGE = [-1 for _ in range(N)]
    stack = [0]
    for i in range(1, N):
        while stack and A[stack[-1]] < A[i]:
            NGE[stack.pop()] = A[i]
        stack.append(i)
    print(*NGE)

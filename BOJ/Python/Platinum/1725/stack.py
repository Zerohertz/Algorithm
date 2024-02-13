import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N = int(read())
    values = [0 for _ in range(N)]
    for i in range(N):
        values[i] = int(read())
    stack = []
    result = 0
    for i in range(N + 1):
        while stack and (i == N or values[stack[-1]] > values[i]):
            height = values[stack[-1]]
            stack.pop()
            width = i
            if stack:
                width = i - stack[-1] - 1
            result = max(result, width * height)
        stack.append(i)
    print(result)

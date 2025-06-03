import sys

read = sys.stdin.readline

if __name__ == "__main__":
    while True:
        values = list(map(int, read().split()))
        N = len(values)
        if values[0] == 0 and N == 1:
            break
        values = values[1:]
        stack = []
        result = 0
        for i in range(N):
            while stack and (i == N - 1 or values[stack[-1]] > values[i]):
                height = values[stack[-1]]
                stack.pop()
                width = i
                if stack:
                    width = i - stack[-1] - 1
                result = max(result, width * height)
            stack.append(i)
        print(result)

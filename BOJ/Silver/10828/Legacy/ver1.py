N = int(input())
stack = []

for _ in range(N):
    l = input().split()
    if l[0] == 'push':
        stack.append(int(l[1]))
    elif l[0] == 'pop':
        if len(stack) > 0:
            print(stack[-1])
            del stack[-1]
        else:
            print(-1)
    elif l[0] == 'size':
        print(len(stack))
    elif l[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

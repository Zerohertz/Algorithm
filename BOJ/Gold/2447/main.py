import sys

N = int(sys.stdin.readline())

def recur(N):
    if N == 1:
        return ['*']
    tmp = recur(N // 3)
    l = []
    for t in tmp:
        l.append(t * 3)
    for t in tmp:
        l.append(t + ' ' * (N // 3) + t)
    for t in tmp:
        l.append(t * 3)
    return l

print('\n'.join(recur(N)))
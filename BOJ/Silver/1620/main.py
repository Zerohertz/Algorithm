import sys

read = sys.stdin.readline

N, M = map(int, read().split())

d = dict()
for i in range(N):
    tmp = read().rstrip()
    d[i + 1] = tmp
    d[tmp] = i + 1

for i in range(M):
    tmp = read().rstrip()
    try:
        tmp = int(tmp)
        print(d[tmp])
    except BaseException:
        print(d[tmp])

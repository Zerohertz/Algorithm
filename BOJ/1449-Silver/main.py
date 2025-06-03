import sys

read = sys.stdin.readline

N, L = map(int, read().split())
loc = sorted(map(int, read().split()))

cnt = 1
tmp = L - 1

for i in range(1, N):
    if loc[i] - loc[i - 1] <= tmp:
        tmp -= loc[i] - loc[i - 1]
    else:
        tmp = L - 1
        cnt += 1

print(cnt)

import sys

read = sys.stdin.readline

N, M = map(int, read().split())
l = list(map(int, read().split()))

bot, top = 1, max(l)
while bot <= top:
    res = 0
    mid = (bot + top) // 2
    for i in range(N):
        if l[i] > mid:
            res += l[i] - mid
    if res >= M:
        bot = mid + 1
    else:
        top = mid - 1
print(top)

import sys

read = sys.stdin.readline

N, M = map(int, read().split())
l = list(map(int, read().split()))

p = []
m = []
cnt = []

for i in l:
    if i > 0:
        p.append(i)
    else:
        m.append(abs(i))

p.sort(reverse=True)
m.sort(reverse=True)

for i in range(len(p) // M):
    cnt.append(p[i * M])
if len(p) % M > 0:
    cnt.append(p[(len(p) // M) * M])

for i in range(len(m) // M):
    cnt.append(m[i * M])
if len(m) % M > 0:
    cnt.append(m[(len(m) // M) * M])

cnt.sort()

res = cnt.pop()
res += 2 * sum(cnt)
print(res)

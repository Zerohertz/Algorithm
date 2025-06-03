N = int(input())
l = []

for i in range(N):
    l.append(list(map(int, input().split())))

l.sort(key=lambda x: (x[1], x[0]))

last = 0
cnt = 0

for i in range(len(l)):
    if l[i][0] >= last:
        last = l[i][1]
        cnt += 1

print(cnt)

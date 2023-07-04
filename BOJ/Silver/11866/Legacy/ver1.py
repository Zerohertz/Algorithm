N, K = map(int, input().split())

l = [1] + [0 for i in range(N)]

print('<', end='')
tmp = 0
for i in range(N):
    localtmp = 0
    while localtmp < K:
        if l[tmp % N + 1] == 0:
            localtmp += 1
        tmp += 1
    if tmp > N:
        tmp = tmp % N
    l[tmp] = 1
    if i < N - 1:
        print(str(tmp) + ',', end=' ')
    else:
        print(str(tmp), end='')
print('>')

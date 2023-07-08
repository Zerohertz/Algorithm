N = int(input())
M = int(input())
l = sorted(map(int, input().split()))

idx1 = 0
idx2 = N - 1
tmp = l[idx1] + l[idx2]
cnt = 0

while True:
    if tmp < M:
        tmp -= l[idx1]
        idx1 += 1
        tmp += l[idx1]
    elif tmp > M:
        tmp -= l[idx2]
        idx2 -= 1
        tmp += l[idx2]
    else:
        cnt += 1
        idx1 += 1
        idx2 -= 1
        tmp = l[idx1] + l[idx2]
    if idx1 >= idx2:
        break

print(cnt)

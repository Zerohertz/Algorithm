N = int(input())
res = 0
while N != 0:
    if N < 0:
        res = -1
        break
    if N % 5 == 0:
        res += N // 5
        N = 0
    else:
        N -= 3
        res += 1

print(res)
import math

N = int(input())
cnt = 0
for x in str(math.factorial(N))[::-1]:
    if x != '0':
        break
    cnt += 1
print(cnt)

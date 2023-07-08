N = int(input())
noList = list(map(int, input().split()))

tmp = 0

if N == len(noList):
    for i in range(N):
        for j in range(2, noList[i] + 1):
            if noList[i] == j:
                tmp += 1
            elif noList[i] % j == 0:
                break

print(tmp)

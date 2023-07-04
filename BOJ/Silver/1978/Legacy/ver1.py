def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] == False
    return [i for i in range(2, n) if sieve[i] == True]


N = int(input())
noList = list(map(int, input().split()))
pList = prime_list(max(noList) + 1)

tmp = 0

if N == len(noList):
    for i in noList:
        for j in pList:
            if i == j:
                tmp += 1

print(tmp)

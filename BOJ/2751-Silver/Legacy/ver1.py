def swapList(l, a, b):
    tmp = l[a]
    l[a] = l[b]
    l[b] = tmp
    return l


N = int(input())

noList = []

for i in range(N):
    noList.append(int(input()))

for i in range(N - 1):
    for j in range(i + 1, N):
        if i != j:
            if noList[i] > noList[j]:
                noList = swapList(noList, i, j)

for i in range(N):
    print(noList[i])

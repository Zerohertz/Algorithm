def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp
    return l


N = int(input())

x = []
y = []

for i in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(N - 1):
    for j in range(i + 1, N):
        if x[i] > x[j]:
            x = swap(x, i, j)
            y = swap(y, i, j)
        elif x[i] == x[j]:
            if y[i] > y[j]:
                x = swap(x, i, j)
                y = swap(y, i, j)

for i in range(N):
    print(x[i], y[i])

N = int(input())
l = list(map(int, input().split()))

if N == 1:
    print("A")
elif N == 2:
    if l[0] == l[1]:
        print(l[0])
    else:
        print("A")
else:
    if l[1] - l[0] == 0:
        a = 0
        b = l[1]
    else:
        a = (l[2] - l[1]) // (l[1] - l[0])
        b = l[1] - l[0] * a
    flag = True
    for i in range(1, N):
        if l[i] == l[i - 1] * a + b:
            continue
        else:
            flag = False
            break
    if flag:
        print(l[N - 1] * a + b)
    else:
        print("B")

N = int(input())
for _ in range(N):
    S = input()
    tmp = 0
    for i in range(len(S)):
        if S[i] == "(":
            tmp += 1
        elif S[i] == ")":
            tmp -= 1
        if tmp < 0:
            tmp = -100
    if tmp == 0:
        print("YES")
    else:
        print("NO")

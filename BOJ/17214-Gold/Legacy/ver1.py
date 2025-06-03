st = input().split("+")
res = ""

for i in range(len(st)):
    if st[i][-1] == "x":
        tmp = int(st[i][:-1]) / 2
        res = str(int(tmp)) + "xx"
    else:
        if len(res):
            res += "+" + str(int(st[i][:])) + "x"
        else:
            res += str(int(st[i][:])) + "x"
res += "+W"

print(res)

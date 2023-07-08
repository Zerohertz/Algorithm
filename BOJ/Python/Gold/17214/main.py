st = input()
tmp = ""
status = False
res = ""

try:
    iszero = int(st)
except BaseException:
    iszero = 1

for i in range(len(st)):
    if "x" in st:
        if st[i] == "x":
            if int(tmp) // 2 == 1:
                res = "xx"
            elif int(tmp) // 2 == -1:
                res = "-xx"
            else:
                res = str(int(tmp) // 2) + "xx"
            tmp = ""
            status = True
        else:
            if status:
                tmp += st[i]
                if i + 1 == len(st):
                    if int(tmp) == 1:
                        res += "+x"
                    elif int(tmp) == -1:
                        res += "-x"
                    else:
                        res += tmp + "x"
            else:
                tmp += st[i]
    else:
        tmp += st[i]
        if i + 1 == len(st):
            if int(tmp) == 1:
                res = "x"
            elif int(tmp) == -1:
                res = "-x"
            else:
                res += tmp + "x"

if iszero == 0:
    res = "W"
else:
    res += "+W"

print(res)

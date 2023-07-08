while True:
    str = input()
    if str == ".":
        break
    s = []
    tmp = True
    for i in str:
        if i == "(" or i == "[":
            s.append(i)
        elif i == ")":
            if not s or s[-1] == "[":
                tmp = False
                break
            elif s[-1] == "(":
                s.pop()
        elif i == "]":
            if not s or s[-1] == "(":
                tmp = False
                break
            elif s[-1] == "[":
                s.pop()
    if tmp == True and not s:
        print("yes")
    else:
        print("no")

def turnT(T, b):
    if b == 1:
        tmp = T[-1]
        del T[-1]
        T.insert(0, tmp)
    elif b == -1:
        tmp = T[0]
        del T[0]
        T.append(tmp)
    return T


def checkM(Tl, Tr):
    if Tl[2] == Tr[6]:
        return False
    else:
        return True


def convertB(b):
    if b == 1:
        return -1
    elif b == -1:
        return 1
    elif b == 0:
        return 0


def dupL(L):
    return [i for i in L]


def returnScore(T1, T2, T3, T4):
    sc = 0
    if T1[0] == '1':
        sc += 1
    if T2[0] == '1':
        sc += 2
    if T3[0] == '1':
        sc += 4
    if T4[0] == '1':
        sc += 8
    return sc


T1 = list(input())
T2 = list(input())
T3 = list(input())
T4 = list(input())

K = int(input())

for _ in range(K):
    a, b = map(int, input().split())
    if a == 1:
        t1 = T1
        T1 = turnT(T1, b)
        if checkM(t1, T2):
            b = convertB(b)
            t2 = dupL(T2)
            T2 = turnT(T2, b)
        else:
            b = 0
        if checkM(t2, T3):
            b = convertB(b)
            t3 = dupL(T3)
            T3 = turnT(T3, b)
        else:
            b = 0
        if checkM(t3, T4):
            b = convertB(b)
            T4 = turnT(T4, b)
    elif a == 2:
        t2 = T2
        T2 = turnT(T2, b)
        db = b
        if checkM(T1, t2):
            db = convertB(db)
            T1 = turnT(T1, db)
        if checkM(t2, T3):
            b = convertB(b)
            t3 = dupL(T3)
            T3 = turnT(T3, b)
        else:
            b = 0
        if checkM(t3, T4):
            b = convertB(b)
            T4 = turnT(T4, b)
    elif a == 3:
        t3 = T3
        T3 = turnT(T3, b)
        db = b
        if checkM(T2, t3):
            b = convertB(b)
            t2 = dupL(T2)
            T2 = turnT(T2, b)
        else:
            b = 0
        if checkM(T1, t2):
            b = convertB(b)
            T1 = turnT(T1, b)
        if checkM(t3, T4):
            db = convertB(db)
            T4 = turnT(T4, db)
    elif a == 4:
        t4 = T4
        T4 = turnT(T4, b)
        if checkM(T3, t4):
            b = convertB(b)
            t3 = dupL(T3)
            T3 = turnT(T3, b)
        else:
            b = 0
        if checkM(T2, t3):
            b = convertB(b)
            t2 = dupL(T2)
            T2 = turnT(T2, b)
        else:
            b = 0
        if checkM(T1, t2):
            b = convertB(b)
            T1 = turnT(T1, b)
print(returnScore(T1, T2, T3, T4))

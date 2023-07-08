import math


def rad2deg(rad):
    deg = rad * 180 / math.pi
    return abs(deg)


def mean(list):
    avg = 0
    for i in list:
        avg = avg + i / len(list)
    return avg


def returnAngle(x, y):
    if y == 0:
        if x > 0:
            return 0
        elif x < 0:
            return 180
    if x == 0:
        if y > 0:
            return 90
        elif y < 0:
            return 270
    rad = math.atan(x / y)
    if x > 0 and y > 0:
        return rad2deg(rad)
    elif x < 0 and y > 0:
        return rad2deg(rad) + 90
    elif x < 0 and y < 0:
        return rad2deg(rad) + 180
    elif x > 0 and y < 0:
        return rad2deg(rad) + 270


def returnAngle2(x1, y1, x2, y2):
    a1 = returnAngle(x1, y1)
    a2 = returnAngle(x2, y2)
    resultAngle = [a1, a2]
    return resultAngle


def checkHit(angleCheckList, x1, y1, x2, y2, angleHitList):
    tmp = 0
    angle = returnAngle2(x1, y1, x2, y2)
    if x2 - x1 != 0:
        bias = -x1 * (y2 - y1) / (x2 - x1) + y1
    elif x1 > 0 and x2 > 0:
        bias = -1
    else:
        bias = 1
    for i in angleCheckList:
        if bias >= 0:
            if i >= min(angle) and i <= max(angle):
                angleHitList[tmp] = angleHitList[tmp] + 1
        else:
            if i <= min(angle) or i >= max(angle):
                angleHitList[tmp] = angleHitList[tmp] + 1
        tmp = tmp + 1
    return angleHitList


def returnAvg(x1, y1, x2, y2, angleHitList):
    angleCheckList = [i / 100 for i in range(36001)]
    for i in range(len(x1)):
        angleHitList = checkHit(
            angleCheckList, x1[i], y1[i], x2[i], y2[i], angleHitList
        )
    return mean(angleHitList)


T = int(input())

k = 0
N = []
x1 = []
y1 = []
x2 = []
y2 = []

for i in range(T):
    N.append(int(input()))
    for j in range(N[i]):
        a, b, c, d = map(int, input().split())
        x1.append(a)
        y1.append(b)
        x2.append(c)
        y2.append(d)

avg = []

for i in range(T):
    angleHitList = [0 for i in range(36001)]
    tmpx1 = x1[N[i - 1] * (i): N[i] * (i + 1)]
    tmpy1 = y1[N[i - 1] * (i): N[i] * (i + 1)]
    tmpx2 = x2[N[i - 1] * (i): N[i] * (i + 1)]
    tmpy2 = y2[N[i - 1] * (i): N[i] * (i + 1)]
    avg.append(returnAvg(tmpx1, tmpy1, tmpx2, tmpy2, angleHitList))

for i in range(T):
    print(format(avg[i], ".5f"))

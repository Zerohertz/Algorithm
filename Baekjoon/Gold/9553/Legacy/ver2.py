import math

def rad2deg(rad):
    deg = rad * 180 / math.pi
    return abs(deg)

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

def returnPartialAvg(x1, y1, x2, y2):
    a1 = returnAngle(x1, y1)
    a2 = returnAngle(x2, y2)
    angle = [a1, a2]
    resultAngle = max(angle) - min(angle)
    avg = resultAngle % 180 / 360
    return avg

def returnAvg(x1, y1, x2, y2):
    avg = 0
    for i in range(len(x1)):
        avg = returnPartialAvg(x1[i], y1[i], x2[i], y2[i]) + avg
    return avg

T = int(input())

N = []

for i in range(T):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    N.append(int(input()))
    for j in range(N[i]):
        a, b, c, d = map(int, input().split())
        x1.append(a)
        y1.append(b)
        x2.append(c)
        y2.append(d)
    avg = (returnAvg(x1, y1, x2, y2))
    print(format(avg, '.5f'))
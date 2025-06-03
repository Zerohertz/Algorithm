import sys

read = sys.stdin.readline


def ccw(p1, p2, p3):
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p2[0], p3[1] - p2[1])
    return v1[0] * v2[1] - v1[1] * v2[0]


"""
v1[0] v1[1]
v2[0] v2[1]
"""


def cross(p1, p2, p3, p4):
    a = ccw(p1, p2, p3)
    b = ccw(p1, p2, p4)
    c = ccw(p3, p4, p1)
    d = ccw(p3, p4, p2)
    if a * b == 0 and c * d == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    else:
        if a * b <= 0 and c * d <= 0:
            return 1
    return 0


x1, y1, x2, y2 = map(int, read().split())
p1 = (x1, y1)
p2 = (x2, y2)

x3, y3, x4, y4 = map(int, read().split())
p3 = (x3, y3)
p4 = (x4, y4)

mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

print(cross(p1, p2, p3, p4))

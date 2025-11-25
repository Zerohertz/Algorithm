import math


def solution(X, Y, colors):
    points = []
    for x, y, c in zip(X, Y, colors):
        r = math.sqrt(x**2 + y**2)
        points.append((r, c))
    points.sort()
    ans = red = green = 0
    for i, (r, c) in enumerate(points):
        if c == "R":
            red += 1
        else:
            green += 1
        if red == green:
            if i + 1 < len(points) and points[i + 1][0] == r:
                continue
            ans = red + green
    return int(ans)

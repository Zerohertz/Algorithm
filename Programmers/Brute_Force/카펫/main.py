from itertools import combinations_with_replacement

def solution(brown, yellow):
    l = []
    for i in range(1, brown + yellow + 1):
        if (brown + yellow) % i == 0:
            l.append(i)
    w, h = 1, 1
    for i in combinations_with_replacement(l, 2):
        w = i[1]
        h = i[0]
        if (w - 2) * (h - 2) == yellow and w - 2 > 0:
            break
    return [w, h]
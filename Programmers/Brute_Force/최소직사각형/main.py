def solution(sizes):
    for size in sizes:
        size.sort()
    inv = [[],[]]
    for size in sizes:
        inv[0].append(size[0])
        inv[1].append(size[1])
    w = max(inv[0])
    h = max(inv[1])
    return w*h
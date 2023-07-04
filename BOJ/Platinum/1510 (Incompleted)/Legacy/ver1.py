def euc(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) * 0.5


m, n = map(int, input().split())
N = 0
for x1 in range(m):
    for y1 in range(n):
        for x2 in range(m):
            for y2 in range(n):
                for x3 in range(m):
                    for y3 in range(n):
                        if ((x1 != x2) or (y1 != y2)) and ((x1 != x3) or (
                                y1 != y3)) and ((x2 != x3) or (y2 != y3)):
                            if not ((x1 == x2 and x1 == x3 and x2 == x3) or (
                                    y1 == y2 and y1 == y3 and y2 == y3)):
                                l1 = euc(x1, y1, x2, y2)
                                l2 = euc(x2, y2, x3, y3)
                                l3 = euc(x1, y1, x3, y3)
                                if l1 == l2 or l2 == l3 or l3 == l1:
                                    N += 1

print(int(N / 6))

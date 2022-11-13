import sys
read = sys.stdin.readline

N, B, C = map(int, read().split())
l = list(map(int, read().split()))
l.append(0)
l.append(0)

a = B
b = B + C
c = B + 2 * C
cost = 0

if B <= C:
    print(sum(l) * a)
else:
    for i in range(N):
        if l[i + 1] > l[i + 2]:
            tmp = min(l[i], l[i + 1] - l[i + 2])
            l[i] -= tmp
            l[i + 1] -= tmp
            cost += b * tmp

            tmp = min(l[i], l[i + 1], l[i + 2])
            l[i] -= tmp
            l[i + 1] -= tmp
            l[i + 2] -= tmp
            cost += c * tmp

            tmp = l[i]
            l[i] -= tmp
            cost += a * tmp
        else:
            tmp = min(l[i], l[i + 1], l[i + 2])
            l[i] -= tmp
            l[i + 1] -= tmp
            l[i + 2] -= tmp
            cost += c * tmp

            tmp = min(l[i], l[i + 1])
            l[i] -= tmp
            l[i + 1] -= tmp
            cost += b * tmp

            tmp = l[i]
            l[i] -= tmp
            cost += a * tmp
    print(cost)
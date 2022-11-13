import sys
read = sys.stdin.readline

N = int(read())
l = list(map(int, read().split()))
l.append(0)
l.append(0)

a, b, c = 3, 5, 7
cost = 0

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
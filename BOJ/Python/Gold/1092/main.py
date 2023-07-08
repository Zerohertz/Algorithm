import sys

read = sys.stdin.readline

N = int(read())
cranes = list(map(int, read().split()))
M = int(read())
boxs = list(map(int, read().split()))

cranes.sort(reverse=True)
boxs.sort(reverse=True)

if boxs[0] > cranes[0]:
    print(-1)
else:
    time = 0
    while boxs:
        for crane in cranes:
            for box in boxs:
                if crane >= box:
                    boxs.remove(box)
                    break
        time += 1
    print(time)

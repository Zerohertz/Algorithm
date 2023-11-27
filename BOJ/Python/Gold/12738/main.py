import sys

read = sys.stdin.readline


N = int(read())
A = list(map(int, read().split()))
ser = [-sys.maxsize]

for i in A:
    if ser[-1] < i:
        ser.append(i)
    else:
        left = 0
        right = len(ser)
        while left < right:
            mid = (left + right) // 2
            if ser[mid] < i:
                left = mid + 1
            else:
                right = mid
        ser[left] = i

print(len(ser) - 1)

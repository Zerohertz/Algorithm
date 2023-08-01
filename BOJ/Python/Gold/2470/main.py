import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N = int(read())
    liquid = list(map(int, read().split()))
    liquid.sort()
    idx1, idx2 = 0, N - 1
    res = sys.maxsize
    while True:
        tmp = liquid[idx1] + liquid[idx2]
        if res >= abs(tmp):
            res = abs(tmp)
            l1, l2 = liquid[idx1], liquid[idx2]
        if tmp < 0:
            idx1 += 1
        elif tmp > 0:
            idx2 -= 1
        else:
            break
        if idx1 >= idx2:
            break
    print(l1, l2)

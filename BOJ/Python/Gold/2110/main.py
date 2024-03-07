import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N, C = map(int, read().split())
    coord = [0 for _ in range(N)]
    for i in range(N):
        coord[i] = int(read())
    coord.sort()
    left, right = 1, coord[-1] - coord[0]
    res = 0
    while left <= right:
        mid = (left + right) // 2
        tmp = coord[0]
        cnt = 1
        for i in range(1, N):
            if coord[i] >= tmp + mid:
                cnt += 1
                tmp = coord[i]
        if cnt >= C:
            left = mid + 1
            res = mid
        else:
            right = mid - 1
    print(res)

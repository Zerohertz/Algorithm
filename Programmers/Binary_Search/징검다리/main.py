def min_dist(maps, target):
    cnt = mnt = 0
    for i in range(len(maps) - 1):
        diff = maps[i + 1] - maps[i]
        if mnt + diff < target:
            cnt += 1
            mnt += diff
        else:
            mnt = 0
    return cnt


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    maps = [0] + rocks + [distance]
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        if min_dist(maps, mid) <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

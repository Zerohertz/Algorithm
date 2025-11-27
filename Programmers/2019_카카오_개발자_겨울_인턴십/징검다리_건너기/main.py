def cross(stones, k, target):
    cnt = 0
    for stone in stones:
        if stone < target:
            cnt += 1
            if k <= cnt:
                return False
        else:
            cnt = 0
    return True


def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    while left <= right:
        mid = (left + right) // 2
        if cross(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

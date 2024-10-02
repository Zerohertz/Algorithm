def solution(diffs, times, limit):
    def bisect(level, diffs, times, limit):
        tmp = time_cur = time_prev = 0
        for diff, time in zip(diffs, times):
            time_cur = time
            if diff > level:
                tmp += (diff - level) * (time_cur + time_prev) + time_cur
            else:
                tmp += time_cur
            time_prev = time
        return tmp <= limit

    answer = 1
    left, right = 1, max(diffs)
    while left <= right:
        mid = (left + right) // 2
        if bisect(mid, diffs, times, limit):
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    return answer

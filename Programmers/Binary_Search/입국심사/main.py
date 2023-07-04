def solution(n, times):
    answer = 0
    bot, top = 1, max(times) * n
    while bot <= top:
        mid = (bot + top) // 2
        p = 0
        for time in times:
            p += mid // time
            if p >= n:
                break
        if p >= n:
            answer = mid
            top = mid - 1
        else:
            bot = mid + 1
    return answer

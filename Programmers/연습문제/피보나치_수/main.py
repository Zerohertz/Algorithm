def solution(n):
    answer = [0 for i in range(n + 1)]
    for i in range(n + 1):
        if i == 0 or i == 1:
            answer[i] = i
        else:
            answer[i] = (answer[i - 1] + answer[i - 2]) % 1234567
    return answer[-1]
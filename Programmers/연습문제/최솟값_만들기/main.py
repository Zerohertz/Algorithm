def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i, j in zip(A, B):
        answer += i * j
    return answer

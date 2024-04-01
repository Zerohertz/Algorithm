def solution(ingredient):
    answer = 0
    tmp = []
    for ing in ingredient:
        tmp.append(ing)
        if tmp[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                tmp.pop()
    return answer

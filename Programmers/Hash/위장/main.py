def solution(clothes):
    d = {}
    for cloth in clothes:
        try:
            d[cloth[1]].append(cloth[0])
        except:
            d[cloth[1]] = [cloth[1]]
    tmp = 1
    for i in d.keys():
        tmp *= len(d[i]) + 1
    answer = tmp - 1
    return answer
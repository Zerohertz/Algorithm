from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        ord = {}
        for order in orders:
            for tmporder in combinations(sorted(order), c):
                tmp = ''.join(tmporder)
                if tmp in ord:
                    ord[tmp] += 1
                else:
                    ord[tmp] = 1
        for tmporder in ord:
            if ord[tmporder] == max(ord.values()) and ord[tmporder] > 1:
                answer.append(tmporder)
    answer.sort()
    return answer
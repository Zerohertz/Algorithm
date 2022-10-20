from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        price = prices.popleft()
        tmp = 0
        for p in prices:
            tmp += 1
            if price > p:
                break
        answer.append(tmp)
    return answer
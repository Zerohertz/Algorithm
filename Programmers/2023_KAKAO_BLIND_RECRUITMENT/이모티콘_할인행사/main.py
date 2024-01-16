from itertools import product


def solution(users, emoticons):
    sales = [10, 20, 30, 40]
    emoji = [[0 for _ in range(len(emoticons))] for _ in range(4)]
    for i, sale in enumerate(sales):
        for j, price in enumerate(emoticons):
            emoji[i][j] = price * (100 - sale) / 100
    results = []
    for sales_ in product([0, 1, 2, 3], repeat=len(emoticons)):
        cnt = prc = 0
        for buy, plu in users:
            user_buy = 0
            for idx, sale in enumerate(sales_):
                if buy <= sales[sale]:
                    user_buy += emoji[sale][idx]
            if plu <= user_buy:
                cnt += 1
            else:
                prc += user_buy
        results.append((cnt, prc))
    return sorted(results, reverse=True)[0]

def solution(n):
    tmp = n + 1
    b = bin(n).count('1')
    while True:
        if bin(tmp).count('1') == b:
            break
        tmp += 1
    return tmp
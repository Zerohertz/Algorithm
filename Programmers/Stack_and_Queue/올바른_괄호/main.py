def solution(s):
    tmp = 0
    for i in list(s):
        if i == '(':
            tmp += 1
        elif i == ')':
            tmp -= 1
        if tmp < 0:
            return False
    if tmp == 0:
        return True
    else:
        return False

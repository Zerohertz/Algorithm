# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.8.10
    words = S.split()
    res = 0

    for word in words:
        alphabet = 0
        numeric = 0
        status = True
        for chr in word:
            tmp = ord(chr)
            if 65 <= tmp <= 90 or 97 <= tmp <= 122:
                alphabet += 1
            elif 48 <= tmp <= 57:
                numeric += 1
            else:
                status = False
                continue
        if status and alphabet % 2 == 0 and numeric % 2 != 0:
            res = max(res, alphabet + numeric)

    if res == 0:
        return -1
    return res

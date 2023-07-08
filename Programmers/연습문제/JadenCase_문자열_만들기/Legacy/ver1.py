def solution(s):
    answer = ""
    l = s.split(" ")
    answer = ""
    for i in l:
        tmp = 0
        for j in i:
            if tmp == 0:
                if ord(j) >= 97 and ord(j) <= 122:
                    answer += chr(ord(j) - 32)
                    tmp = 1
                else:
                    answer += j
                    tmp = 1
            else:
                if ord(j) >= 65 and ord(j) <= 90:
                    answer += chr(ord(j) + 32)
                else:
                    answer += j
        answer += " "
    answer = answer.strip()
    return answer

def solution(s):
    answer = ''
    l = s.split(' ')
    answer = ''
    for i in range(len(l)):
        l[i] = l[i].capitalize()
    answer = ' '.join(l)
    return answer

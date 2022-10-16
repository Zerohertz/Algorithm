def solution(array, commands):
    answer = []
    for command in commands:
        tmparr = array[command[0] - 1:command[1]]
        tmparr.sort()
        answer.append(tmparr[command[2] - 1])
    return answer
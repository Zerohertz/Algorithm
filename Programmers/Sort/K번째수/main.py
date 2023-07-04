def solution(array, commands):
    answer = []
    for command in commands:
        tmparr = sorted(array[command[0] - 1:command[1]])
        answer.append(tmparr[command[2] - 1])
    return answer

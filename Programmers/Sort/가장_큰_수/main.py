def solution(numbers):
    numarr = list(map(str, numbers))
    numarr.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numarr)))

import sys

N = int(sys.stdin.readline())

noList = [i for i in range(1, N + 1)]

while len(noList) > 1:
    del noList[0]
    tmp = noList[0]
    del noList[0]
    noList.append(tmp)
print(noList[0])

def returnChoi(l, N):
  dic = dict()
  for i in range(1, N + 1):
    dic[i] = []
  maxCnt = 1
  cnt = 1
  for i in range(1, N):
    if l[i] == l[i - 1]:
      cnt += 1
    else:
      dic[cnt].append(l[i - 1])
      if maxCnt < cnt:
        maxCnt = cnt
        cnt = 1
    if i == N - 1:
      dic[cnt].append(l[i])
      if maxCnt < cnt:
        maxCnt = cnt
  if N == 1:
    dic[1].append(l[0])
  dic[maxCnt].sort()
  if len(dic[maxCnt]) == 1:
    print(dic[maxCnt][0])
  else:
    print(dic[maxCnt][1])

N = int(input())
l = []

for i in range(N):
  l.append(int(input()))

l.sort()
print(round(sum(l) / N))
print(l[N // 2])
returnChoi(l, N)
print(l[-1] - l[0])
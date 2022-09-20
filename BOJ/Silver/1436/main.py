N = int(input())
cnt = 1
tmp = 665

while N >= cnt:
  tmp += 1
  if '666' in str(tmp):
    cnt += 1

print(tmp)
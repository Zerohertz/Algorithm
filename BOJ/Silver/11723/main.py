import sys
read = sys.stdin.readline

N = int(read())
l = set()

for _ in range(N):
  tmp = read().split()
  if tmp[0] == 'add':
    l.add(int(tmp[1]))
  elif tmp[0] == 'remove':
    try:
      l.remove(int(tmp[1]))
    except:
      continue
  elif tmp[0] == 'check':
    if int(tmp[1]) in l:
      print(1)
    else:
      print(0)
  elif tmp[0] == 'toggle':
    if int(tmp[1]) in l:
      l.remove(int(tmp[1]))
    else:
      l.add(int(tmp[1]))
  elif tmp[0] == 'all':
    l = set([i for i in range(1, 21)])
  elif tmp[0] == 'empty':
    l = set()
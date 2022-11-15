import sys
from collections import deque
read = sys.stdin.readline

T = int(read())
for _ in range(T):
  commands = read().rstrip()
  n = int(read())
  l = read().rstrip()
  if n > 0:
    d = deque(list(map(str, l[1:-1].split(','))))
  else:
    d = deque()
  status = True
  rev = 0
  for command in commands:
    if command == 'R':
      rev += 1
    elif command == 'D':
      if n > 0:
        if rev % 2 == 0:
          d.popleft()
        else:
          d.pop()
        n -= 1
      else:
        status = False
        print('error')
        break
  if rev % 2 == 1:
    d.reverse()
  if status:
    print('[' + ','.join(d) + ']')
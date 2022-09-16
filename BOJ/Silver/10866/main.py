import sys

N = int(sys.stdin.readline())
Deque = []

for _ in range(N):
  l = sys.stdin.readline().split()
  if l[0] == 'push_front':
    Deque.insert(0, int(l[1]))
  elif l[0] == 'push_back':
    Deque.append(int(l[1]))
  elif l[0] == 'pop_front':
    if len(Deque) > 0:
      print(Deque[0])
      del Deque[0]
    else:
      print(-1)
  elif l[0] == 'pop_back':
    if len(Deque) > 0:
      print(Deque[-1])
      del Deque[-1]
    else:
      print(-1)
  elif l[0] == 'size':
    print(len(Deque))
  elif l[0] == 'empty':
    if len(Deque) == 0:
      print(1)
    else:
      print(0)
  elif l[0] == 'front':
    if len(Deque) > 0:
      print(Deque[0])
    else:
      print(-1)
  elif l[0] == 'back':
    if len(Deque) > 0:
      print(Deque[-1])
    else:
      print(-1)
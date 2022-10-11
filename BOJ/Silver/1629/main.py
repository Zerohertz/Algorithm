import sys
read = sys.stdin.readline

def power(A, B):
  if B == 0:
    return 1
  elif B == 1:
    return A % C
  else:
    tmp = power(A, B // 2)
    if B % 2 == 0:
      return (tmp * tmp) % C
    else:
      return (tmp * tmp * A) % C

A, B, C = map(int, read().split())
print(power(A, B))
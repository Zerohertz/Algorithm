import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
K = int(read())
apple = []

for _ in range(K):
    a, b = map(int, read().split())
    a -= 1
    b -= 1
    apple.append((b, a))

L = int(read())
timeline = {}
for _ in range(L):
    a, b = read().split()
    a = int(a)
    timeline[a] = b

snake = deque([(0, 0)])
dir_x, dir_y = 1, 0
time = 0

rightTurn = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
leftTurn = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}

while True:
    x, y = snake[0]
    if time in timeline.keys():
        if timeline[time] == "L":
            dir_x, dir_y = leftTurn[(dir_x, dir_y)]
        elif timeline[time] == "D":
            dir_x, dir_y = rightTurn[(dir_x, dir_y)]
    nx, ny = x + dir_x, y + dir_y
    if (nx, ny) in snake:
        print(time + 1)
        break
    elif not ((0 <= nx < N) and (0 <= ny < N)):
        print(time + 1)
        break
    elif (nx, ny) in apple:
        apple.remove((nx, ny))
        snake.appendleft((nx, ny))
    else:
        snake.pop()
        snake.appendleft((nx, ny))
    time += 1

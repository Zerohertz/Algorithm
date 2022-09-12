d = [[0 for j in range(10)] for i in range(10)]
for i in range(10):
    d[i][:] = input().split()
hungry = 1
tmp = [1, 1]
while hungry > 0:
    if d[tmp[0]][tmp[1]] == '2':
        hungry = hungry - 1
    d[tmp[0]][tmp[1]] = '9'
    if d[tmp[0]][tmp[1]+1] != '1':
        tmp[1] = tmp[1] + 1
    elif d[tmp[0]+1][tmp[1]] != '1':
        tmp[0] = tmp[0] + 1
    else:
        hungry = 0
for i in range(10):
    for j in range(10):
        print(d[i][j], end = ' ')
    print()
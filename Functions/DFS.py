visit = [False for _ in range(len(maps))]

def DFS(start):
  visit[start] = True
  for i in maps[start]:
    if not visit[i]:
      DFS(i)
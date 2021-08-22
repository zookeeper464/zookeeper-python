from collections import deque

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dic = dict()
cnt = 2
dr,dc = [1,-1,0,0],[0,0,1,-1]
visited = [[False for _ in range(n)] for _ in range(n)]

def bfs (q,cnt):
  global dic, visited
  temp_q = deque()
  while q:
    r,c = q.popleft()
    s = False

    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
        if lst[nr][nc] == 0:
          s = True
        elif lst[nr][nc] == 1:
          q.append([nr,nc])
          visited[nr][nc] = True

    if s:
      temp_q.appendleft([r,c])
      lst[r][c] = cnt
  return temp_q

for r in range(n):
  for c in range(n):
    if lst[r][c] == 1 and not visited[r][c]:
      visited[r][c] = True
      q = deque([[r,c]])
      dic[cnt] = bfs(q,cnt)
      cnt += 1


def check ():
  answer = 0
  while True:
    answer += 2
    temp_list = list(dic.keys())
    for t in temp_list:
      q = dic[t]
      for _ in range(len(q)):
        r,c = q.popleft()
        for i in range(4):
          nr,nc = r+dr[i],c+dc[i]
          if 0<=nr<n and 0<=nc<n:
            temp = lst[nr][nc]
            if temp == 0:
              q.append([nr,nc])
              lst[nr][nc] = t
            elif temp > t:
              return(answer-2)
            elif 1< temp < t:
              return(answer-1)
print(check())

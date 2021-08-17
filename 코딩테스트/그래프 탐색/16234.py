from collections import deque

n,l,r = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]

def bfs (q, visited):
  global lst
  temp_lst = []
  total = 0
  num = 0

  while q:
    tr, tc = q.popleft()
    temp_lst.append([tr,tc])
    total += lst[tr][tc]
    num += 1

    for i in range(4):
      nr,nc = tr+dr[i],tc+dc[i]
      if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
        if l<=abs(lst[tr][tc]-lst[nr][nc])<=r:
          visited[nr][nc] = True
          q.append([nr,nc])
  
  turn = total//num
  for tr, tc in temp_lst:
    lst[tr][tc] = turn
  
  return visited

def check():
  global lst
  s = True
  cnt = -1

  while s:
    cnt += 1
    s = False
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
      for j in range(n):
        temp = lst[i][j]

        for k in range(0,4,2):
          nr,nc = i+dr[k],j+dc[k]
          if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
            if l<=abs(temp-lst[nr][nc])<=r:
              q = deque([[nr,nc]])
              visited[nr][nc] = True
              visited = bfs(q, visited)
              s = True
    
  return cnt

print(check())

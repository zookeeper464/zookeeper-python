from collections import deque

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
switch = True
answer = 0

def bfs (q):
  while q:
    r,c = q.popleft()
    zeros = 0
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
        if lst[nr][nc] > 0:
          visited[nr][nc] = True
          q.append([nr,nc])
        elif lst[nr][nc] == 0:
          zeros += 1

    if lst[r][c] -zeros <= 0:
      lst[r][c] = -1
    else:
      lst[r][c] = lst[r][c]-zeros

while switch:
  visited = [[False for _ in range(m)] for _ in range(n)]
  cnt = 0

  for r in range(1,n-1):
    for c in range(1,m-1):
      if not visited[r][c] and lst[r][c]>0:
        visited[r][c] = True
        q = deque([[r,c]])
        bfs(q)
        cnt += 1
  
  if cnt != 1:
    if cnt == 0:
      answer = 0
    break

  answer += 1

  for r in range(1,n-1):
    for c in range(1,m-1):
      if lst[r][c] == -1:
        lst[r][c] = 0

print(answer)

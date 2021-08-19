from collections import deque

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
sec = -1

def bfs(q, visited):
  while q:
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<nr<n-1 and 0<nc<m-1 and lst[nr][nc]>0 and visited[nr][nc] == -1:
        q.append([nr,nc])
        temp = 0
        for j in range(4):
          tr,tc = nr+dr[j],nc+dc[j]
          if lst[tr][tc] == 0:
            temp += 1
        visited[nr][nc] = temp

  return visited

while True:
  sec += 1
  cnt = 0
  visited = [[-1 for _ in range(m)] for _ in range(n)]
  for r in range(1,n-1):
    for c in range(1,m-1):
      if lst[r][c] != 0 and visited[r][c] == -1:
        cnt += 1
        q = deque([[r,c]])
        visited = bfs(q, visited)

  if cnt == 0:
    print(0)
    break
  elif cnt >= 2:
    print(sec)
    break

  for r in range(1,n-1):
    for c in range(1,m-1):
      if visited[r][c]>0:
        lst[r][c] = max(lst[r][c]-visited[r][c],0)

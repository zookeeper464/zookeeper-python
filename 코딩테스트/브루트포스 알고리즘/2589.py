from collections import deque

n,m = map(int,input().split())
lst = [list(input()) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
start = []
answer = 0

def bfs (q):
  count = -1
  visited = [[False for _ in range(m)] for _ in range(n)]
  visited[q[0][0]][q[0][1]] = True

  while q:
    count += 1
    for _ in range(len(q)):
      r, c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<m and lst[nr][nc] == 'L' and not visited[nr][nc]:
          q.append([nr,nc])
          visited[nr][nc] = True
  return count


for r in range(n):
  for c in range(m):
    if lst[r][c] == 'L':
      q = deque([[r,c]])
      cnt = 0
      
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<m and lst[nr][nc] == 'L':
          cnt += 1
      
      if len(q)<=2:
        answer = max(answer,bfs(q))

print(answer)

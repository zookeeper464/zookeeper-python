"""from collections import deque

n, m = map(int,input().split())
lst = [list(input()) for _ in range(n)]
dp = []
for i in range(n):
  for j in range(m):
    if lst[i][j] =="1":
      dp.append([i,j])
dr, dc = [1,0,-1,0],[0,1,0,-1]
answer = n*m

for r1,c1 in dp:
  visited = [[False for _ in range(m)] for _ in range(n)]
  visited[0][0] = True
  cnt = 0
  lst[r1][c1] = "0"
  q = deque([[0,0]])
  s = False
  while q:
    cnt += 1
    for _ in range(len(q)):
      r,c = q.popleft()
      if (r, c) == (n-1,m-1):
        q = deque()
        s = True
        break
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]

        if 0<=nr<n and 0<=nc<m:
          if lst[nr][nc]=="0" and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append([nr,nc])

  lst[r1][c1] = "1"
  if s:
    answer = min(answer,cnt)

if answer<m*n or m*n == 1:
  print(answer)
else:
  print(-1)"""
# DFS로 풀어야 가능한 문제

from collections import deque

n,m = map(int,input().split())
dp =[list(map(int,input().split())) for _ in range(n)]
zeros, virus = 0, []
dr,dc = [1,-1,0,0],[0,0,1,-1]

for r in range(n):
  for c in range(n):
    if dp[r][c] == 0:
      zeros += 1
    elif dp[r][c] == 2:
      virus.append([r,c])
v = len(virus)
answer = 2500

def dfs(cnt,idx,lst):
  if cnt == m:
    bfs(lst)
    return
  
  for i in range(idx+1,v):
    dfs(cnt+1,i,lst+[i])

def bfs(lst):
  global answer, zeros
  visited = [[False for _ in range(n)] for _ in range(n)]
  num = zeros
  q = deque()
  
  for i in lst:
    q.append(virus[i])

  cnt = 0
  while q:
    if num == 0:
      if answer > cnt:
        answer = cnt
      return

    for _ in range(len(q)):
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]

        if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
          if dp[nr][nc] == 0:
            q.append([nr,nc])
            visited[nr][nc] = True
            num -= 1
            
          if dp[nr][nc] == 2:
            q.append([nr,nc])
            visited[nr][nc] = True

    cnt += 1

dfs(0,-1,[])
print(answer if answer != 2500 else -1)

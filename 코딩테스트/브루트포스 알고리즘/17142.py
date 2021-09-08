from collections import deque

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
virus = []
answer, zero = 2500, 0
dr,dc = [1,-1,0,0],[0,0,1,-1]

for r in range(n):
  for c in range(n):
    if lst[r][c] == 2:
      virus.append((r,c))
    elif lst[r][c] == 0:
      zero += 1
v = len(virus)

def bfs(q,z):
  cnt = 0
  visited = [[0 for _ in range(n)] for _ in range(n)]
  temp_lst = []
  while q:
    if cnt > answer:
      return cnt

    if z == 0:
      return cnt  

    for _ in range(len(q)):
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<n and visited[nr][nc]==0 and lst[nr][nc] != 1:
          visited[nr][nc] = cnt+1
          q.append((nr,nc))
          if lst[nr][nc] == 0:
            z -= 1

    cnt += 1

  if z == 0:
    return cnt

  return 2500
  
def dfs(cnt,lst,idx):
  global answer
  if cnt == m:
    q = deque()
    for l in lst:
      q.append(virus[l])
    b = bfs(q,zero)
    if answer > b:
      answer = b
    return

  for i in range(idx+1,v):
    lst.append(i)
    dfs(cnt+1,lst,i)
    lst.pop()

dfs(0,[],-1)
if answer == 2500:
  print(-1)
else:
  print(answer)

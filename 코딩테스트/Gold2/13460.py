from collections import deque

n,m = map(int, input().split())
lst = [list(input()) for _ in range(n)]
visited =[[[[11]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
for r in range(n):
  for c in range(m):
    if lst[r][c] == 'R':
      lst[r][c] = '.'
      rr,rc = r,c
    elif lst[r][c] == 'B':
      lst[r][c] = '.'
      br,bc = r,c
visited[rr][rc][br][bc] = 0
dr,dc = [1,-1,0,0],[0,0,1,-1]
answer = 11

def move (rr,rc,br,bc,look,num):
  global answer
  cnt,switch = 0, True
  ddr,ddc = dr[look],dc[look]
  while lst[rr+ddr][rc+ddc] == '.':
    rr += ddr
    rc += ddc
    cnt += 1
    
  while lst[br+ddr][bc+ddc] == '.':
    br += ddr
    bc += ddc
    cnt -= 1
  
  if lst[br+ddr][bc+ddc] == 'O':
    switch = False

  if (rr,rc) == (br,bc):
    if cnt>0:
      rr -= ddr
      rc -= ddc
    else:
      br -= ddr
      bc -= ddc
  
  if switch and lst[rr+ddr][rc+ddc] == 'O':
    answer = min(answer,num)
  
  return rr,rc,br,bc,switch

def dfs(rr,rc,br,bc,cnt):
  if cnt == 10:
    return

  for i in range(4):
    nrr,nrc,nbr,nbc,switch = move(rr,rc,br,bc,i,cnt+1)
    if switch and visited[nrr][nrc][nbr][nbc] > cnt:
      visited[nrr][nrc][nbr][nbc] = cnt
      dfs(nrr,nrc,nbr,nbc,cnt+1)

dfs(rr,rc,br,bc,0)
print(answer if answer!=11 else -1)

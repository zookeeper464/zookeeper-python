from collections import deque

n, m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(m)]
q = deque()
dr, dc = [1,0,-1,0],[0,1,0,-1] 

for r in range(m):
  for c in range(n):
    if lst[r][c] == 1:
      q.append([r,c])
    elif lst[r][c] == -1:
      lst[r][c] = 1
      
t = 0
while q:
  l = len(q)
  for _ in range(l):
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<m and 0<=nc<n and lst[nr][nc] == 0:
        q.append([nr,nc])
        lst[nr][nc] = 1
  t += 1

s = 0
for r in range(m):
  s += sum(lst[r])

if s == n*m:
  print(t-1)
else:
  print(-1)

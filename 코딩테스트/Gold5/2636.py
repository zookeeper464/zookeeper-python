from collections import deque

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
q,lst[0][0] = deque([[0,0]]),2
num = 0

def air (q):
  while q:
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<m and lst[nr][nc] == 0:
        q.append([nr,nc])
        lst[nr][nc] = 2

for r in range(n):
  for c in range(m):
    if lst[r][c] == 1:
      num += 1

air(q)

t = 0
while True:
  t += 1
  cnt = 0
  for r in range(n):
    for c in range(m):
      if lst[r][c] == 1:
        for i in range(4):
          nr,nc = r+dr[i],c+dc[i]
          if lst[nr][nc] == 2:
            lst[r][c] = 0
            cnt += 1
            break

  for r in range(n):
    for c in range(m):
      if lst[r][c] == 0:
        for i in range(4):
          nr,nc = r+dr[i],c+dc[i]
          if lst[nr][nc] == 2:
            lst[r][c] = 2
            air(deque([[r,c]]))
            break

  num -= cnt
  if num == 0:
    break
  print(num,cnt,t)
  print(*lst,sep='\n')
  
print(t)
print(cnt)

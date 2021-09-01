from collections import deque

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
zero1,zero2 = [], []
virus = []
answer = 0
dr,dc = [1,-1,0,0],[0,0,1,-1]

for r in range(n):
  for c in range(m):
    if lst[r][c] == 0:
      zero1.append(r)
      zero2.append(c)
    elif lst[r][c] == 2:
      virus.append([r,c])
z = len(zero1)

def dfs (i,j,k,q,l):
  global answer
  l[zero1[i]][zero2[i]] = 1
  l[zero1[j]][zero2[j]] = 1
  l[zero1[k]][zero2[k]] = 1


  while q:
    for _ in range(len(q)):
      r, c = q.popleft()
      for x in range(4):
        nr,nc = r+dr[x],c+dc[x]
        if 0<=nr<n and 0<=nc<m and l[nr][nc] == 0:
          q.append([nr,nc])
          l[nr][nc] = 2
  
  temp = 0
  for r in range(n):
    for c in range(m):
      if l[r][c] == 0:
        temp += 1

  return temp

for i in range(z-2):
  for j in range(i+1,z-1):
    for k in range(j+1,z):
      l = [ll[:] for ll in lst]
      v = virus[:]
      t = dfs(i,j,k,deque(v),l)
      if answer < t:
        answer = t

print(answer)

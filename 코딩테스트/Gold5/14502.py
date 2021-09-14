from collections import deque

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
two,zero, answer = [], [], 0
for r in range(n):
  for c in range(m):
    if lst[r][c] == 0:
      zero.append([r,c])
    elif lst[r][c] == 2:
      two.append([r,c])
z = len(zero)
dr,dc = [1,-1,0,0],[0,0,1,-1]

def check(aa,bb,cc,z):
  global answer, two
  visited = [[False for _ in range(m)] for _ in range(n)]
  for r,c in (aa,bb,cc):
    visited[r][c] = True
  q = deque(two)

  while q:
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and lst[nr][nc] == 0:
        visited[nr][nc] = True
        z -= 1
        q.append([nr,nc])
        if z<answer:
          return
  
  if answer < z:
    print(answer,z,aa,bb,cc)
    answer = z

for aa in range(z-2):
  for bb in range(aa+1,z-1):
    for cc in range(bb+1,z):
      check(zero[aa],zero[bb],zero[cc],z-3)

print(answer)

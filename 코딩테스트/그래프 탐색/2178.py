from collections import deque

n,m = map(int,input().split())
mat = []
for _ in range(n):
  mat.append(list(map(int,list(input()))))
dc,dr = [1,0,-1,0],[0,1,0,-1]

q = deque([[0,0]])
mat[0][0] = 2
answer = -1
cnt = 1
while q:
  cnt += 1
  for _ in range(len(q)):
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<m and mat[nr][nc] == 1:
        q.append([nr,nc])
        mat[nr][nc] = 2
  if mat[n-1][m-1] == 2:
    answer = cnt
    break
    
print(answer)

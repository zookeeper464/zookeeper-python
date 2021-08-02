from collections import deque

n = int(input())
mat = []
for _ in range(n):
  mat.append(list(map(int,list(input()))))
dc,dr = [1,0,-1,0],[0,1,0,-1]

def check(q):
  global mat
  num = 0
  while q:
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<n and mat[nr][nc] == 1:
        q.append([nr,nc])
        mat[nr][nc] = 2
        num += 1
  return max(1,num)
cnt = 0
answer = [] 
for i in range(n):
  for j in range(n):
    if mat[i][j] == 1:
      cnt += 1
      q = deque([[i,j]])
      answer.append(check(q))

answer.sort()
print(cnt)
for ans in answer:
  print(ans)

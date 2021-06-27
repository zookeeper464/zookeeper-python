from collections import deque

n,l,t = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
cnt = -1

def check (q,s,num):
  global temp_lst
  dr,dc = [0,1,0,-1],[1,0,-1,0]
  while q:
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<n and temp_lst[nr][nc] < 0:
        if l<=lst[r][c]-lst[nr][nc]<=t or l<=lst[nr][nc]-lst[r][c]<=t:
          q.append([nr,nc])
          temp_lst[nr][nc] = 0
          s += lst[nr][nc]
          num += 1
  m = s//num
  for i in range(n):
    for j in range(n):
      if temp_lst[i][j] == 0:
        temp_lst[i][j] = m

while True:
  temp_lst = [[-1 for _ in range(n)] for i in range(n)]
  for i in range(n):
    for j in range(n):
      if temp_lst[i][j]<0:
        if i<n-1 and l<=abs(lst[i][j]-lst[i+1][j])<=t:
          q = deque([[i,j],[i+1,j]])
          temp_lst[i][j],temp_lst[i+1][j] = 0,0
          check(q,lst[i][j]+lst[i+1][j],2)
        elif j<n-1 and l<=abs(lst[i][j]-lst[i][j+1])<=t:
          q = deque([[i,j],[i,j+1]])
          temp_lst[i][j],temp_lst[i][j+1] = 0,0
          check(q,lst[i][j]+lst[i][j+1],2)
  c = False
  for i in range(n):
    for j in range(n):
      if temp_lst[i][j]>=0:
        lst[i][j] = temp_lst[i][j]
        c = True
  cnt += 1

  if not c:
    break

print(cnt)

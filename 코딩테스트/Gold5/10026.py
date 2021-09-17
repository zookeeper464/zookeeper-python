from collections import deque

n = int(input())
lst = [list(input().rstrip()) for _ in range(n)]
visited1 = [[False for _ in range(n)] for _ in range(n)]
visited2 = [[False for _ in range(n)] for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
a,b = 0,0

def check1(q,s):
  while q:
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<n and not visited1[nr][nc] and lst[nr][nc] == s:
        visited1[nr][nc] = True
        q.append([nr,nc])


def check2(q,s):
  if s == 'B':
    while q:
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<n and not visited2[nr][nc] and lst[nr][nc] == "B":
          visited2[nr][nc] = True
          q.append([nr,nc])
  
  else:
    while q:
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<n and not visited2[nr][nc] and lst[nr][nc] != 'B':
          visited2[nr][nc] = True
          q.append([nr,nc])

for r in range(n):
  for c in range(n):
    if visited1[r][c] == False:
      q =deque([[r,c]])
      check1(q,lst[r][c])
      a+=1

    if visited2[r][c] == False:
      q =deque([[r,c]])
      check2(q,lst[r][c])
      b+=1
  
print(a,b)

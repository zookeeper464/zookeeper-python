from collections import deque

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,-1,1]
q = deque([[0,0]])

num = 0
for i in range(n):
  num += sum(lst[i])

def check (q):
  global lst
  while q:
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<m and lst[nr][nc] == 0:
        lst[nr][nc] = 2
        q.append([nr,nc])

check(q)

tim = 0
while True:
  cnt = 0
  for r in range(n):
    for c in range(m):
      if lst[r][c] == 1:
        s = False
        for i in range(4):
          if lst[r+dr[i]][c+dc[i]] == 2:
            s = True
            break
        if s:
          cnt += 1
          lst[r][c] = 0

  for r in range(n):
    for c in range(m):
      if lst[r][c] == 0:
        s = False
        for i in range(4):
          if lst[r+dr[i]][c+dc[i]] == 2:
            s = True
            break
        if s:
          lst[r][c] = 2
          q = deque([[r,c]])
          check(q)

  if cnt > 0:
    num -= cnt
    tim += 1
    if num == 0:
      print(tim, cnt, sep='\n')
      break

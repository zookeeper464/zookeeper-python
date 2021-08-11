from collections import deque

n = int(input())
lst = [list(input()) for _ in range(n)]
visited1 = [[False for _ in range(n)] for _ in range(n)]
visited2 = [[False for _ in range(n)] for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]

def bfs1 (r,c, temp1):
  global visited1
  q = deque([[r,c]])
  while q:
    tr, tc = q.popleft()
    for i in range(4):
      nr,nc = tr+dr[i],tc+dc[i]
      if 0<=nr<n and 0<=nc<n:
         if lst[nr][nc] == temp1 and not visited1[nr][nc]:
          visited1[nr][nc] = True
          q.append([nr,nc])

def bfs2 (r,c,temp2):
  global visited2
  q = deque([[r,c]])
  if temp2 == 'B':
    while q:
      tr, tc = q.popleft()
      for i in range(4):
        nr,nc = tr+dr[i],tc+dc[i]
        if 0<=nr<n and 0<=nc<n and lst[nr][nc] == temp2 and not visited2[nr][nc]:
          visited2[nr][nc] = True
          q.append([nr,nc])
  else:
    while q:
      tr, tc = q.popleft()
      for i in range(4):
        nr,nc = tr+dr[i],tc+dc[i]
        if 0<=nr<n and 0<=nc<n and lst[nr][nc] in 'RG' and not visited2[nr][nc]:
          visited2[nr][nc] = True
          q.append([nr,nc])


cnt1, cnt2 = 0,0
for r in range(n):
  for c in range(n):
    if not visited1[r][c]:
      visited1[r][c] = True
      bfs1(r,c, lst[r][c])
      cnt1 += 1

    if not visited2[r][c]:
      visited2[r][c] = True
      bfs2(r,c, lst[r][c])
      cnt2 += 1

print(cnt1, cnt2)

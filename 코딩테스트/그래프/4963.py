from collections import deque

dc, dr = [1,1,1,0,0,-1,-1,-1],[1,0,-1,1,-1,1,0,-1]
answer = []

while True:
  m,n = map(int,input().split())
  if (n,m) == (0,0):
    break
  lst = [list(map(int,input().split())) for _ in range(n)]
  cnt = 0
  for r in range(n):
    for c in range(m):
      if lst[r][c] == 1:
        lst[r][c] = 0
        cnt += 1
        q =deque([[r,c]])
        while q:
          for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(8):
              nr, nc = x+dc[i], y+dr[i]
              if 0<=nr<n and 0<=nc<m and lst[nr][nc]==1:
                q.append([nr,nc])
                lst[nr][nc] = 0
  answer.append(cnt)

for i in answer:
  print(i)

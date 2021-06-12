from collections import deque

dc,dr = [1,0,-1,0],[0,1,0,-1]
t = int(input())
answer = []
for _ in range(t):
  m,n,k = map(int,input().split())
  lst = [[0 for _ in range(m)] for _ in range(n)]
  for _ in range(k):
    x,y = map(int,input().split())
    lst[y][x] = 1
  
  cnt = 0
  for r in range(n):
    for c in range(m):
      if lst[r][c] == 1:
        lst[r][c] = 0
        cnt+=1
        q = deque([[r,c]])
        while q:
          for _ in range(len(q)):
            temp = q.popleft()
            for k in range(4):
              nr,nc = temp[0]+dr[k],temp[1]+dc[k]
              if 0<=nr<n and 0<=nc<m and lst[nr][nc]==1:
                q.append([nr,nc])
                lst[nr][nc] = 0
  answer.append(cnt)

for i in answer:
  print(i)

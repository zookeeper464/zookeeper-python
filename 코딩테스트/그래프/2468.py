from collections import deque

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dc, dr = [1,0,-1,0], [0,1,0,-1]
answer = 0

for i in range(n):
  for j in range(n):
    if lst[i][j] > 4:
      answer += 1
      q = deque([[i,j]])
      while q:
        r,c = q.popleft()
        lst[r][c] = 4
        for k in range(4):
          nr,nc = r+dr[k],c+dc[k]
          if 0<=nr<n and 0<=nc<n and lst[nr][nc]>4:
            q.append([nr,nc])

print(answer)

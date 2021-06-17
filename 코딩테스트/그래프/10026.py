from collections import deque

n = int(input())
dp1 = [list(input()) for _ in range(n)]
dp2 = [dp1[i][:] for i in range(n)]
dx, dy = [1,0,-1,0],[0,1,0,-1]
cnt1, cnt2 = 0,0

for i in range(n):
  for j in range(n):
    if dp1[i][j] in "RGB":
      cnt1 += 1
      temp = dp1[i][j]
      q = deque([[i,j]])
      dp1[i][j] = "a"
      while q:
        x,y = q.popleft()
        for k in range(4):
          nx,ny = x+dx[k],y+dy[k]
          if 0<=nx<n and 0<=ny<n and dp1[nx][ny] == temp:
            dp1[nx][ny] = "a"
            q.append([nx,ny])

for i in range(n):
  for j in range(n):
    if dp2[i][j] in "RGB":
      cnt2 += 1
      temp = dp2[i][j]
      if temp in "RG":
        temp = "RG"
      q = deque([[i,j]])
      while q:
        x,y = q.popleft()
        for k in range(4):
          nx,ny = x+dx[k],y+dy[k]
          if 0<=nx<n and 0<=ny<n and dp2[nx][ny] in temp:
            dp2[nx][ny] = "a"
            q.append([nx,ny])

print(cnt1, cnt2)

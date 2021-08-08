from collections import deque

m, n, h = map(int, input().split())
dp = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

answer = -1
dx,dy,dz = [1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]
q = deque()

for z in range(h):
  for y in range(n):
    for x in range(m):
      if dp[z][y][x] == 1:
        q.append([z,y,x])

while q:
  answer += 1
  for i in range(len(q)):
    th,r,c = q.popleft()
    for i in range(6):
      nh,nr,nc = th+dz[i],r+dy[i],c+dx[i]
      if 0<=nh<h and 0<=nr<n and 0<=nc<m and dp[nh][nr][nc] == 0:
        dp[nh][nr][nc] = 1
        q.append([nh,nr,nc])

s = True
for i in dp:
  if not s:
    break
  for j in i:
    if 0 in j:
      count = -1
      s = False
      break
if s:
  print(answer)
else:
  print(-1)

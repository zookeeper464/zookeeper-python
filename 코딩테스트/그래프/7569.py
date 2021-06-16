from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
#x,y,z
dp = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

wall,answer = 0,-1
dx,dy,dz = [1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]
q = deque()

for z in range(h):
  for y in range(n):
    for x in range(m):
      if dp[z][y][x] == -1:
        wall += 1
      elif dp[z][y][x] == 1:
        q.append([z,y,x])

if not q:
  answer += 1

while q:
  answer += 1
  for i in range(len(q)):
    t,r,c = q.popleft()
    for i in range(6):
      nh,nr,nc = t+dz[i],r+dy[i],c+dx[i]
      if 0<=nh<h and 0<=nr<n and 0<=nc<m and dp[nh][nr][nc] == 0:
        dp[nh][nr][nc] = 1
        q.append([nh,nr,nc])

s = True

for l1 in dp:
  if not s:
    break
  for l2 in l1:
    if 0 in l2:
      s = False
      break

if s:
  print(answer)
else:
  print(-1)

from collections import deque
import sys
INF = sys.maxsize

k,(w,h) = int(input()), map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(h)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
dh,dw = [-2,-2,-1,-1,1,1,2,2],[1,-1,2,-2,2,-2,1,-1]
q = deque([[0,0,k]])
dp = [[[INF for _ in range(k+1)] for _ in range(w)] for _ in range(h)]
for i in range(k+1):
  dp[0][0][i] = 0

while q:
  r,c,num = q.popleft()
  for i in range(4):
    nr,nc = r+dr[i],c+dc[i]
    if 0<=nr<h and 0<=nc<w and lst[nr][nc] == 0 and dp[nr][nc][num]>dp[r][c][num]+1:
      dp[nr][nc][num] = dp[r][c][num]+1
      q.append([nr,nc,num])
  
  if num>0:
    for i in range(8):
      nr,nc = r+dh[i],c+dw[i]
      if 0<=nr<h and 0<=nc<w and lst[nr][nc] == 0 and dp[nr][nc][num-1]>dp[r][c][num]+1:
        dp[nr][nc][num-1] = dp[r][c][num]+1
        q.append([nr,nc,num-1])

answer = min(dp[-1][-1])
print(answer if answer != INF else -1)

from collections import deque
import sys
INF = sys.maxsize

m,n = map(int, input().split())
lst = [list(map(int,input())) for _ in range(n)]
dp = [[INF]*m for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]

q = deque([[0,0]])
dp[0][0] = 0

while q:
  r,c = q.popleft()
  for i in range(4):
    nr,nc = r+dr[i],c+dc[i]
    if 0 <=nr<n and 0<=nc<m and dp[nr][nc]==INF:
      if lst[nr][nc] == 0:
        dp[nr][nc] = dp[r][c]
        q.appendleft([nr,nc])
      else:
        dp[nr][nc] = dp[r][c] + 1
        q.append([nr,nc])

print(dp[n-1][m-1])

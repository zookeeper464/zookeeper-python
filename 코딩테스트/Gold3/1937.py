n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]

def dfs(r,c):
  if dp[r][c] != -1:
    return dp[r][c]

  dp[r][c] = 1
  for i in range(4):
    nr,nc = r+dr[i],c+dc[i]
    if 0<=nr<n and 0<=nc<n and lst[r][c]>lst[nr][nc]:
      if dp[nr][nc] == -1:
        dp[r][c] = max(dp[r][c],dfs(nr,nc)+1)
      elif dp[r][c]<=dp[nr][nc]:
        dp[r][c] = dp[nr][nc]+1

  return dp[r][c]

answer = 0
for r in range(n):
  for c in range(n):
    temp = dfs(r,c)
    answer = max(temp,answer)

print(answer)

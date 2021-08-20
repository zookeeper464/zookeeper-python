n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dr, dc = [1,-1,0,0],[0,0,1,-1]
answer = 0

def dfs (r,c):
  if dp[r][c]:
    return dp[r][c]

  dp[r][c] = 1

  for i in range(4):
    nr,nc = r+dr[i],c+dc[i]
    if 0<=nr<n and 0<=nc<n and lst[r][c]<lst[nr][nc]:
      dp[r][c] = max(dp[r][c], dfs(nr,nc)+1)

  return dp[r][c]

for r in range(n):
  for c in range(n):
    answer = max(answer,dfs(r,c))

print(answer)

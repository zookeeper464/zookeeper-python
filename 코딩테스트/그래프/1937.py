import sys
sys.setrecursionlimit(40000)
input = sys.stdin.readline

n = int(input())
dp = [[-1 for _ in range(n)] for _ in range(n)]
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [0,1,0,-1],[1,0,-1,0]

def check (r,c):
  global dp
  if dp[r][c] >= 0:
    return dp[r][c]
  dp[r][c] = 1
  for i in range(4):
    nr,nc = r+dr[i],c+dc[i]
    if 0<=nr<n and 0<=nc<n and lst[r][c]<lst[nr][nc]:
      if dp[nr][nc]>0: 
        dp[r][c] = max(dp[nr][nc]+1,dp[r][c])
      else:
        dp[r][c] = max(dp[r][c],check(nr,nc)+1)
  return dp[r][c]

answer = 0
for r in range(n):
  for c in range(n):
    answer = max(answer,check(r,c))


print(answer)

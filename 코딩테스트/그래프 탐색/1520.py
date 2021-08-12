import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

m,n=map(int,input().split())
lst=[list(map(int, input().split())) for i in range(m)]
dp=[[-1]*n for i in range(m)]
dr,dc =[1,-1,0,0],[0,0,1,-1]

def dfs(r,c):
  if (r,c) == (0,0):
    return 1
  if dp[r][c] == -1:
    dp[r][c] = 0
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<m and 0<=nc<n:
        if lst[r][c] < lst[nr][nc]:
          dp[r][c] += dfs(nr,nc)
  return dp[r][c]

print(dfs(m-1,n-1))

n,m = map(int,input().split())
dp = [[-1 for _ in range(m)] for _ in range(n)]
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]

def check(r,c):
  if (r,c) == (0,0):
    return 1

  temp = 0
  for i in range(4):
    nr,nc = r+dr[i],c+dc[i]

    if 0<=nr<n and 0<=nc<m and lst[r][c]<lst[nr][nc]:
      if dp[nr][nc] == -1:
        dp[nr][nc] = check(nr,nc)

      temp += dp[nr][nc]
  
  return temp

print(check(n-1,m-1))

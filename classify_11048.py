n,m=map(int,input().split())
dp=[[0]*m for i in range(n)]
lst=[]
for i in range(n):
  ls=list(map(int,input().split()))
  lst.append(ls)

for i in range(n):
  for j in range(m):
    dp[i][j]+=lst[i][j]+max(dp[i-1][j],dp[i][j-1])

print(dp[n-1][m-1])

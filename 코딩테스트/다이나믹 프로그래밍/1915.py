n,m = map(int,input().split())
dp = [list(map(int,list(input()))) for _ in range(n)]
answer = 0

for i in range(1,n):
  for j in range(1,m):
    if dp[i][j] == 1:
      dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
      answer = max(dp[i][j],answer)

print(answer)

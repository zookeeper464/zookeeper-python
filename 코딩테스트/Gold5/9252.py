s1,s2 = input(), input()
n,m = len(s1), len(s2)
dp = [['' for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
  for j in range(m):
    if s1[i]==s2[j]:
      dp[i][j] = dp[i-1][j-1]+s1[i]
    else:
      if len(dp[i-1][j])>len(dp[i][j-1]):
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i][j-1]

print(len(dp[-2][-2]),dp[-2][-2],sep='\n')

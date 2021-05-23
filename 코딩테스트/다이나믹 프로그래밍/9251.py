s1 = input()
s2 = input()
n = len(s1)
m = len(s2)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
  for j in range(m):
    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    if s1[i] == s2[j]:
      dp[i+1][j+1] += 1

print(dp[-1][-1])

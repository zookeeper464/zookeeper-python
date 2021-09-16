s1,s2 = input(), input()
l1,l2 = len(s1), len(s2)
dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

for r in range(l1):
  for c in range(l2):
    if s1[r] == s2[c]:
      dp[r][c] = dp[r-1][c-1]+1
    else:
      dp[r][c] = max(dp[r-1][c],dp[r][c-1])

print(dp[-2][-2])

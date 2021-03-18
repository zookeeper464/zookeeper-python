lst1 = list(input())
lst2 = list(input())

n1, n2 = len(lst1), len(lst2)
dp=[[""] * (n2+1) for i in range(n1+1)]
for i in range(n1):
  for j in range(n2):
    if lst1[i] == lst2[j]:
      dp[i+1][j+1] = dp[i][j] + lst1[i]
    else:
      if len(dp[i][j + 1]) > len(dp[i + 1][j]):
        dp[i + 1][j + 1] = dp[i][j + 1]
      else:
        dp[i + 1][j + 1] = dp[i + 1][j]

print(len(dp[-1][-1]))
print(dp[-1][-1])

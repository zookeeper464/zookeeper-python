s1 = input()
s2 = input()
n1, n2 = len(s1), len(s2)
lst1, lst2 = list(s1), list(s2)
dp = [["" for _ in range(n2+1)] for _ in range(n1+1)]

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

import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
dp = [[0] * len(s2) for i in range(len(s1))]
#비교를 위한 dp 준비와 입력

m = 0
for i in range(len(s1)):
  for j in range(len(s2)):
    if s1[i] == s2[j]:
      if i == 0 or j == 0:
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j-1] + 1
        if m < dp[i][j]:
          m = dp[i][j]
    else:
      dp[i][j] = 0      

print(m)

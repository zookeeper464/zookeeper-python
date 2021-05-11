t = int(input())
answer = []

dp = [[0 for i in range(15)] for j in range(15)]
for i in range(1,15):
  dp[0][i] = i
  dp[1][i] = i*(i+1)//2

for i in range(2,15):
  for j in range(1,15):
    for k in range(1,j+1):
      dp[i][j] += dp[i-1][k]

for i in range(t):
  k = int(input())
  n = int(input())
  answer.append(dp[k][n])

for i in answer:
  print(i)

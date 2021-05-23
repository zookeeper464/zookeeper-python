n = int(input())
dp = [0 for i in range(n+1)]
dp[0] = 1
for i in range(n+1):
  if i%2==0:
    for j in range(i-2):
      dp[i] += dp[j]*2
    dp[i] += 3*dp[i-2]

print(dp)

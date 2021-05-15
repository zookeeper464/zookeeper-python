n = int(input())
dp = [n+1 for _ in range(n+1)]
lst = [i**2 for i in range(1, int(n**0.5)+1)]
for i in lst:
  dp[i] = 1

for i in range(2,n+1):
  if dp[i] == n+1:
    for j in lst:
      if j<i and dp[i]>dp[i-j]+1:
        dp[i]=dp[i-j]+1

print(dp[n])

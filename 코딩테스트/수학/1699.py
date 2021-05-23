n = int(input())
m = int(n**0.5)
dp = [0 for _ in range(n+1)]
for i in range(m):
  temp = (m-i)*(m-i)
  dp[temp] = 1
  for idx,v in enumerate(dp):
    if v != 0 and idx+temp<n+1:
      if dp[idx+temp] == 0:
        dp[idx+temp] = v+1
      else:
        dp[idx+temp] = min(v+1,dp[idx+temp])
print(dp[-1])

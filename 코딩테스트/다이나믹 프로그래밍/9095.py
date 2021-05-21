t = int(input())
lst = []
for _ in range(t):
  lst.append(int(input()))
m = max(lst)
dp = [0 for _ in range(m+1)]
dp[1],dp[2],dp[3]=1,2,4
for i in range(4,m+1):
  dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
for i in lst:
  print(dp[i])

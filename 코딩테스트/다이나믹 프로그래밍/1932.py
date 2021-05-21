n = int(input())
dp = list(map(int,input().split()))
for i in range(n-1):
  lst = list(map(int,input().split()))
  lst[0] += dp[0]
  for j in range(i):
    lst[j+1] += max(dp[j],dp[j+1])
  lst[-1] += dp[-1]
  dp = lst[:]

print(max(dp))

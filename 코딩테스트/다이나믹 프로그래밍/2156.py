n = int(input())
lst = [0]
for _ in range(n):
  lst.append(int(input()))
dp = lst[:]
if n>1:
  dp[2] += dp[1]
for i in range(3,n+1):
  dp[i] += max(dp[i-3]+lst[i-1],dp[i-2])
print(max(dp[-1],dp[-2]))

n = int(input())
dp = list(map(int,input().split()))

for i in range(1,n):
  if dp[i] != 0:
    dp[i] = dp[i-1] +1

print(sum(dp))

n = int(input())
lst = list(map(int,input().split()))
dp = lst[:]
for i in range(n):
  for j in range(i):
    if lst[i]>lst[j] and dp[i]<dp[j]+lst[i]:
      dp[i] = dp[j]+lst[i]

print(max(dp))

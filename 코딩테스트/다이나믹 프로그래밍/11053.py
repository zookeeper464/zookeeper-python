n = int(input())
dp = [1 for _ in range(n)]
lst = list(map(int,input().split()))
for i in range(1,n):
  for j in range(i):
    if lst[i]>lst[j] and dp[i]<=dp[j]:
      dp[i] = dp[j]+1
print(max(dp))

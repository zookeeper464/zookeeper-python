lst = list(input())
n = len(lst)
dp = [1 for _ in range(n)]
for i in range(1,n):
  dp[i] = dp[i-1]
  if 0<int(lst[i-1]+lst[i])<27:
    dp[i]+= dp[i-2]
print(dp[-1])

n = int(input())
lst = list(map(int,input().split()))
dp = lst[:]
# 입력을 위한 기본 값들

for i in range(1, n):
  for j in range(i):
    dp[i]  = min(dp[i], dp[j] + lst[i-j-1])

print(dp[-1])

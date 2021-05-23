n, k = map(int,input().split())

dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in range(n):
  a=int(input())
  for i in range(k+1-a):
    if dp[i]!=0:
      dp[a+i]+=dp[i]


print(dp[-1])

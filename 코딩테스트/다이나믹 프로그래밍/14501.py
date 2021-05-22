n = int(input())
days,costs = [], []
for i in range(n):
  d,c = map(int,input().split())
  days.append(d)
  costs.append(c)

dp = [0 for _ in range(n)]
for i in range(n):
  temp = i+days[i]-1
  if temp<n:
    if i>0:
      dp[temp] = max(max(dp[:i])+costs[i],dp[temp])
    else:
      dp[temp] = costs[i]
print(max(dp))

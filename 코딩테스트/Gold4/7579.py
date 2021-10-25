n,m = map(int,input().split())
memories = list(map(int,input().split()))
costs = list(map(int,input().split()))
num = sum(costs)
dp = [[0] * (num+1) for i in range(n)]
answer = num

for i in range(n):
  byte = memories[i]
  cost = costs[i]
  
  for j in range(num+1):
    if j < cost:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + byte)
    
    if dp[i][j] >= m:
      answer = min(answer, j)

print(answer)

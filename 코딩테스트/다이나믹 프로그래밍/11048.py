n,m = map(int,input().split())
lst = []
for i in range(n):
  lst.append(list(map(int,input().split())))
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
  for j in range(m):
    dp[i+1][j+1] = lst[i][j]+max(dp[i][j+1],dp[i+1][j])

print(dp[-1][-1])

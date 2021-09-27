n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for c in range(1,n):
  if lst[0][c] ==1:
    break
  dp[0][c][0] = 1

for r in range(1,n):
  for c in range(1,n):
    if lst[r][c] == 0:
      dp[r][c][0] = dp[r][c-1][0]+dp[r][c-1][1]
      dp[r][c][2] = dp[r-1][c][1]+dp[r-1][c][2]

      if lst[r][c-1]+lst[r-1][c] == 0:
        dp[r][c][1] = sum(dp[r-1][c-1])

print(sum(dp[-1][-1]))

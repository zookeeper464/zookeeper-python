import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = []
for i in range(n):
  lst.append(list(map(int,input().split())))

dp = [[0] * (m+1) for i in range(n+1)]

for i in range(n):
  for j in range(m):
    if j == 0:
      dp[i+1][j+1] = lst[i][j]
    else:
      dp[i+1][j+1] = lst[i][j] + dp[i+1][j]
  
  for j in range(m):
    dp[i+1][j+1] += dp[i][j+1]


k = int(input())

answer = []
for l in range(k):
  i,j,x,y = map(int,input().split())
  i -= 1
  j -= 1
  answer.append(dp[x][y]-dp[x][j]-dp[i][y]+dp[i][j])

for i in answer:
  print(i)

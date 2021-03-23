t = int(input())
lst =[]

for i in range(t):
  n = int(input())
  lst.append(n)
m = max(lst)
#입력하기 위한 준비

dp = [[0]*4 for i in range(max(4,m+1))]
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1
if m > 3:
  for i in range(4,m+1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3])%1000000009
    dp[i][2] = (dp[i-2][3] + dp[i-2][1])%1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2])%1000000009
#자료를 생성하기 위한 데이터 베이스 생성

for i in lst:
  print(sum(dp[i])%1000000009)

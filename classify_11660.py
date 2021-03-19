import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dp = [[0]*(n+1)]
for i in range(n):
  s = list(map(int,input().split()))
  for j in range(1,n):
    s[j]=s[j-1]+s[j]
  s=[0]+s
  dp.append(s)
for i in range(2, n+1):
  for j in range(1, n+1):
    dp[i][j]+=dp[i-1][j]


answer = []
for i in range(m):
  a, b, c, d = map(int,input().split())
  temp = dp[c][d]+dp[a-1][b-1]-dp[c][b-1]-dp[a-1][d]
  answer.append(temp)

for i in answer:
  print(i)

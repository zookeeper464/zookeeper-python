n = int(input())
lst = []
m = 0
for i in range(n):
  a = int(input())
  lst.append(a)
  if m < a:
    m = a

dp = [0,1,2,4]
for i in range(m-3):
  dp.append((dp[-1]+dp[-2]+dp[-3])%1000000009)

for i in lst:
  print(dp[i])

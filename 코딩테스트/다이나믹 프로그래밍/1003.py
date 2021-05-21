t = int(input())
lst = []
for _ in range(t):
  lst.append(int(input()))
m = max(lst)
dp = [0, 1]
for i in range(2,m+1):
  dp.append(dp[i-1]+dp[i-2])
for i in lst:
  if i == 0:
    print(1, 0)
  else:
    print(dp[i-1], dp[i])

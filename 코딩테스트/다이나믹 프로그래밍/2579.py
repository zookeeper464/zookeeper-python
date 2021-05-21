n = int(input())
lst = []
for _ in range(n):
  lst.append(int(input()))
dp = lst[:]
if n>1:
  dp[1] += lst[0]
if n>2:
  dp[2] += max(lst[1],lst[0])

for i in range(3,n):
  dp[i] += max(dp[i-2],dp[i-3]+lst[i-1])

print(dp[-1])

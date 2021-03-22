n = int(input())
lst = [0]
for i in range(n):
  ls = int(input())
  lst.append(ls)

dp = [1]*(n+1)
# 증가하는 수열을 찾기 위한 준비

for i in range(2, n+1):
  for j in range(1,i):
    if lst[j] < lst[i] and dp[j]+1 > dp[i]:
      dp[i] = dp[j]+1
#각 위치에서 증가하는 수열의 길이가 가장 긴 수열의 길이

print(n-max(dp))

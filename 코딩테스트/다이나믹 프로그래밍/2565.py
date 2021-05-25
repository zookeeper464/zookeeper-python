n = int(input())
temp = []
for _ in range(n):
  temp.append(list(map(int,input().split())))

temp.sort()
lst = []
for i in temp:
  lst.append(i[1])

dp = [1 for _ in range(n)]
for i in range(1,n):
  for j in range(i):
    if lst[i]>lst[j] and dp[i]<dp[j]+1:
      dp[i] = dp[j]+1

print(n-max(dp))

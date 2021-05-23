n = int(input())
lst = list(map(int,input().split()))
dp1, dp2 = [1 for _ in range(n)], [1 for _ in range(n)]
for i in range(1,n):
  for j in range(i):
    if lst[i]>lst[j] and dp1[i]<dp1[j]+1:
      dp1[i] = dp1[j]+1

for i in range(n-2,-1,-1):
  for j in range(n-1,i,-1):
    if lst[i]>lst[j] and dp2[i]<dp2[j]+1:
      dp2[i] = dp2[j]+1

dp = [dp1[i]+dp2[i] for i in range(n)]
print(max(dp)-1)

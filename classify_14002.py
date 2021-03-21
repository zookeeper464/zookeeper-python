n = int(input())
lst = [0]+list(map(int, input().split()))
dp = [0]*(n+1)
visit = [-1]*(n+1)
 
for i in range(1,n+1):
  for j in range(1, i):
    if lst[i] > lst[j] and dp[i] < dp[j]:
      dp[i] = dp[j]
      visit[i] = j
  dp[i] += 1
 
print(max(dp))

ans = []
max_idx = dp.index(max(dp))
while max_idx != -1:
  ans.append(lst[max_idx])
  max_idx = visit[max_idx]
ans.reverse()
 
print(' '.join(map(str, ans)))

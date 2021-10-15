n = int(input())
lst = list(map(int, input().split()))
dp = [1]*(n)
visited = [-1]*(n)
max_idx,max_val = 0,0
 
for i in range(n):
  for j in range(i):
    if lst[i]>lst[j] and dp[i]<=dp[j]:
      dp[i] = dp[j]+1
      visited[i] = j
  
  if max_val < dp[i]:
    max_idx, max_val = i, dp[i]

ans = []
while max_idx != -1:
  ans.append(lst[max_idx])
  max_idx = visited[max_idx]

print(max_val) 
print(*ans[::-1])

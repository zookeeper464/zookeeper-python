from collections import deque

n = int(input())
lst = [[] for _ in range(n+1)]

for _ in range(n-1):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)

dp = [0] * (n+1)
dp[1] = -1
q = deque([1])
while q:
  temp = q.popleft()
  for i in lst[temp]:
    if dp[i] == 0:
      dp[i] = temp
      q.append(i)

for i in range(2,n+1):
  print(dp[i])

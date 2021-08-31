from collections import deque

n,m = map(int,input().split())
stairs = [1 for _ in range(n+1)]
dp = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  dp[b].append(a)

mx = 0
lst = []
for i in range(1,n+1):
  if dp[i]:
    visited = [0] * (n+1)
    visited[i] = 1
    q = deque([i])
    cnt = 1
    while q:
      for _ in range(len(q)):
        temp = q.popleft()
        for j in dp[temp]:
          if visited[j] == 0:
            visited[j] = 1
            q.append(j)
            cnt += 1
    
    if cnt>=mx:
      if cnt != mx:
        mx = cnt
        lst = []
      lst.append(i)

print(*lst)

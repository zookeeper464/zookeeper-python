from collections import deque

n,m = map(int,input().split())
lst = [set() for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  lst[a].add(b)
  lst[b].add(a)
for i in range(n+1):
  lst[i] = list(lst[i])

answer = n**2
idx = 0
for i in range(1,n+1):
  dp = [-1 for _ in range(n+1)]
  q = deque(lst[i])
  dp[i] = 0
  cnt = 1
  while q:
    for _ in range(len(q)):
      temp = q.popleft()
      if dp[temp] ==-1:
        dp[temp] = cnt
        for j in lst[temp]:
          if dp[j] ==-1:
            q.append(j)
    cnt += 1
  s = sum(dp)+1    
  if answer > s:
    answer = s
    idx = i

print(idx)

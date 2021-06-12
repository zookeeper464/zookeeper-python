from collections import deque

n,m = map(int,input().split())
lst = [[] for _ in range(n+1)]
dp = [False for _ in range(n+1)]
answer = 0

for _ in range(m):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)

for i in range(1,n+1):
  if not dp[i]:
    q = deque([i])
    answer += 1
    while q:
      for _ in range(len(q)):
        temp = q.popleft()
        dp[temp] = True
        for j in lst[temp]:
          if not dp[j]:
            q.append(j)

print(answer)

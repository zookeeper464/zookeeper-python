from collections import deque

n = int(input())
start, end = map(int,input().split())
m = int(input())
lst = [[] for _ in range(n+1)]
dp = [False for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)

q = deque([start])
dp[start] = True
cnt = 0

while q:
  cnt += 1
  for _ in range(len(q)):
    temp = q.popleft()
    for i in lst[temp]:
      if not dp[i]:
        dp[i] = True
        q.append(i)
    if dp[end]:
      q = 1
      break
  
  if q == 1:
    break

if q == 1:
  print(cnt)
else:
  print(-1)

from collections import deque

n,m = map(int,input().split())
lst = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)

answer = 1
num = n*n

for i in range(1,n+1):
  if len(lst[i]) == 1:
    pass
  q = deque([i])
  dp = [0] * (n+1)
  cnt = 0

  while q:
    cnt += 1
    for _ in range(len(q)):
      temp = q.popleft()
      for j in lst[temp]:
        if dp[j] == 0:
          dp[j] = cnt
          q.append(j)

  s = sum(dp)
  if num > s:
    answer = i
    num = s

print(answer)

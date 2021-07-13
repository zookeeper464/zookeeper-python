from collections import deque

t = int(input())
answer = []

for _ in range(t):
  n,m = map(int,input().split())
  lst = list(map(int,input().split()))
  dp = [False] * n
  dp[m] = True
  dq = deque(dp)
  lq = deque(lst)
  rank = 0
  
  while True:
    x = max(lq)
    temp1 = lq.popleft()
    temp2 = dq.popleft()
    if temp1 == x:
      rank += 1
      if temp2:
        break
      pass
    else:
      lq.append(temp1)
      dq.append(temp2)
  answer.append(rank)

for i in answer:
  print(i)

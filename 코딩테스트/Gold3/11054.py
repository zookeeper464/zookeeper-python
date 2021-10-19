n = int(input())
lst = list(map(int,input().split()))
dp,q = [1],[lst[0]]
for i in range(1,n):
  l = len(q)
  for j in range(l-1,-1,-1):
    if q[j]<lst[i]:
      if j == l-1:
        q.append(lst[i])
      else:
        q[j+1]=lst[i]
      break
  else:
    q[0]=lst[i]
  dp.append(len(q))

answer = dp[-1]+1
q = [lst[-1]]
for i in range(n-2,-1,-1):
  l = len(q)
  for j in range(l-1,-1,-1):
    if q[j]<lst[i]:
      if j == l-1:
        q.append(lst[i])
      else:
        q[j+1]=lst[i]
      break
  else:
    q[0]=lst[i]
  answer = max(answer,dp[i]+len(q))
    
print(answer-1)

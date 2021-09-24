n = int(input())
lst = list(map(int,input().split()))
q = []
dp = []

for i in range(n):
  for _ in range(len(q)):
    temp,idx = q.pop()
    if temp>lst[i]:
      q.append((temp,idx))
      q.append((lst[i],i))
      dp.append(idx+1)
      break
  else:
    dp.append(0)
    q.append((lst[i],i))

print(*dp)

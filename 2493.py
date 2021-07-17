n = int(input())
lst = list(map(int,input().split()))
dp,answer = [], []

for i in range(n):
  l = len(dp)
  for j in range(l):
    temp = dp.pop()
    if lst[temp]>lst[i]:
      dp.append(temp)
      answer.append(temp+1)
      break
  if len(dp) == 0:
    answer.append(0)
  dp.append(i)

for ans in answer:
  print(ans, end = ' ')

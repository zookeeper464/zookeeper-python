n = int(input())
lst = list(map(int,input().split()))
dp = []
answer = []
for i in range(n-1,-1,-1):
  temp = -1
  for _ in range(len(dp)):
    temp = dp.pop()
    if lst[i] < temp:
      dp.append(temp)
      break
  if dp == []:
    temp = -1
  dp.append(lst[i])
  answer.append(temp)

for i in range(n-1,-1,-1):
  print(answer[i], end= ' ')

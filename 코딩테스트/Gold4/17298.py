stack = []
n = int(input())
lst = list(map(int,input().split()))
answer = []

for i in range(n-1,-1,-1):
  top = lst[i]
  if not stack:
    answer.append(-1)
    stack.append(top)
    continue
  

  temp = stack.pop()
  while True:
    if top < temp:
      answer.append(temp)
      stack.append(temp)
      stack.append(top)
      break

    if not stack:
      answer.append(-1)
      stack.append(top)
      break

    temp = stack.pop()

for i in range(n-1,-1,-1):
  print(answer[i], end = ' ')

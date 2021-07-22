lst = []
while True:
  s = input()
  if s =='.':
    break
  lst.append(s)

answer = []
for i in lst:
  temp = []
  ans = 'yes'
  for j in i:
    if j == '[' or j =='(':
      temp.append(j)
    elif j == ']':
      if temp and temp[-1] == '[':
        temp.pop()
      else:
        ans = 'no'
        break
    elif j == ')':
      if temp and temp[-1] == '(':
        temp.pop()
      else:
        ans = 'no'
        break
  
  if temp:
    ans = 'no'
  
  answer.append(ans)

for ans in answer:
  print(ans)
